from django.core.exceptions import ValidationError

districts = [
    'Gangtok',
    'Pakyong',
    'Gyalshing',
    'Soreng',
    'Mangan',
    'Namchi'
]

sub_divisions = [
    'Gangtok',
    'Rabdang',
    'Pakyong',
    'Rangpo',
    'Rongli',
    'Dentam',
    'Gyalshing',
    'Yuksom',
    'Soreng',
    'Mangalbaray'
    'Chungthang',
    'Mangan',
    'Kabi',
    'Dzongu',
    'Namchi',
    'Ravangla',
    'Jorethang',
    'Yangtang',
]

blocks = [
    'Khamdong',
    'Martam',
    'Nandok',
    'Rakdong Tintek',
    'Ranka',
    'Pakyong',
    'Parkha',
    'Duga',
    'Rhenock',
    'Reghu',
    'Dentam',
    'Hee Martam',
    'Gyalshing',
    'Yuksom',
    'Arithang Chongrang',
    'Soreng',
    'Baiguney',
    'Chungbong Chakung',
    'Daramdin',
    'Kaluk',
    'Mangalbarey',
    'Chungthang',
    'Mangan',
    'Kabi',
    'Passingdong',
    'Namchi',
    'Temi',
    'Namthang',
    'Wak',
    'Ravangla ',
    'Jorethang',
    'Sumbuk',
    'Yangyang'
]

doclist = [
    'COI',
    'SS',
    'RC'
]


def check_type(_):
    if _ not in doclist:
        raise ValidationError('The type is not supported')


def check_district(_):
    if _ not in districts:
        raise ValidationError('District not validated')


def check_subdivisions(_):
    if _ not in sub_divisions:
        raise ValidationError('Sub Division not validated')


def check_block(_):
    if _ not in blocks:
        raise ValidationError('Block not validated')