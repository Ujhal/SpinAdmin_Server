from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import District,SubDivision,Block
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
import random
# Create your views here.

districts = [
    'Gangtok',
    'Gyalshing',
    'Mangan',
    'Namchi',
    'Soreng',
    'Pakyong'
    
    
    
]

subdivisons = {
    'Gangtok': [ 'Gangtok',
                 'Rabdang',
    ],
    districts[1]: ['Pakyong',
                   'Rangpo',
                   'Rongli',],
    districts[2]: ['Dentam',
                   'Gyalshing',
                   'Yuksom',],
    districts[3]: ['Soreng',
                   'Mangalbarey'],
    districts[4]: ['Chungthang',
                   'Mangan',
                   'Kabi',
                   'Dzongu',],
    districts[5]: ['Namchi',
                   'Ravangla',
                   'Jorethang',
                   'Yangyang',]
}

blocks = {
    'gangtok': ['Gangtok Station', 'Sichey (Old GMC)', 'Chandmari(Old GMC)', 'Sichey', 'Lingdok', 'Ranka', 'Rumtek', 'Samdong', 'Naitam', ],

    'rabdang': ['Rabdang', 'Khamdong', 'Tumin'],

    'pakyong': ['Pakyong', 'Dikling Pacheykhani', 'Aho-Santi', 'Tareythang-Bering', 'Machong', 'Amba-Taza'],

    'rongli': ['Rongli', 'Subaneydara', 'Rhenock'],

    'rangpo': ['Duga', 'West Pandam'],



    'gyalshing': ['Darap', 'Lingchom', 'Gyalshing'],

    'dentam': ['Radhu Khandu', 'Dentam', 'Bermiok', 'Gyaten'],

    'yuksom': ['Gerethang', 'Tashiding', 'Dhupidara', 'Thingling'],


    'soreng': ['Arubotey', 'Chakung', 'Zoom', 'Soreng', 'Okhrey', 'Dodak', 'Sombaria'],

    'mangalbarey': ['Rinchenpong', 'Kaluk', 'Mangalbaria', 'Kamling'],


    'mangan': ['Singhik-Mangan'],

    'kabi': ['Phensong', 'Namok'],

    'dzongu': ['Passingdong', 'Hee-Gyathang', 'Gor'],

    'chungthang': ['Chungthang'],




    'namchi': ['Wak', 'Tarku', 'Damthang', 'Bermiok Tokal', 'Rameng', 'Sadam', 'Rong', 'Boomtar', 'Kitam', 'Namthang', 'Turung', 'Maniram'],

    'jorethang': ['Salghari', 'Poklok', 'Sumbuk', 'Melli Dara'],

    'ravangla': ['Ralong', 'Rabong', 'Kewzing', 'Tinkitam'],

    'yangyang': ['Lingi', 'Lingmo', 'Yangyang']

}

@api_view(['GET'])
def load_districts(request):
    try:
        for d in districts:
            District.objects.update_or_create(name=d)
        return Response(data={'success': True}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(data={'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_districts(request):
    dis = District.objects.all().values_list('name', flat=True)
    return Response(dis)    
       
@api_view(['GET'])
def load_subd(request):
    try:
        for d in subdivisons.keys():
            dist = District.objects.get(name=d)
            for s in subdivisons[d]:
                SubDivision.objects.update_or_create(name=s, district=dist)
        return Response(status=status.HTTP_201_CREATED, data={'Success':True})
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={
            f'{e}'
        })
    
@api_view(['GET'])
def load_block(request,parent):
    try:
        for s in blocks.keys():
            try:
                subs = SubDivision.objects.get(name=s)
                for b in blocks[s]:
                    Block.objects.update_or_create(name=b, subdivision=subs)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'SubDivision not found'})
        return Response(status=status.HTTP_201_CREATED, data={'Success'})
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={
            f'{e,subs.name}'
        })

@api_view(['GET'])
def get_subdivs(request, parent):
    try:
        sub = SubDivision.objects.filter(
            district__name=parent.capitalize()).values_list('name', flat=True)
        return Response(sub)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
    
@api_view(['GET'])
def get_blocks(request, parent):
    try:
        Response('error at getblacks')
        blk = Block.objects.filter(
        subdivision__name=parent).values_list('name', flat=True)
        return Response(blk)
    except Exception as e:
        return Response({'error at getblocks': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def generateSPINid(request, parent): 
    try:
        blkspin = Block.objects.filter(subdivision__name=parent).values('subdivision_id', 'id').first()
        unique_number = random.randint(1000,1999)
        if blkspin:
            return Response({'subdivision_id': blkspin['subdivision_id'], 'id': blkspin['id'],'unique_number': unique_number})
        else:
            return Response({'error': 'Block not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
