from .models import District, SubDivision, Block
from django.core.exceptions import ValidationError


def check_district(_):
    if not District.objects.filter(name=_).exists():
        raise ValidationError('District not validated')


def check_subdivision(_):
    if not SubDivision.objects.filter(name=_).exists():
        raise ValidationError('Sub Division not validated')


def check_block(_):
    if not Block.objects.filter(name=_).exists():
        raise ValidationError('Block not validated')


def get_d_id(_):
    i = District.objects.get(name=_).id
    return str(i) if i not in range(0, 10) else '0' + str(i)


def get_s_id(_):
    i = SubDivision.objects.get(name=_).id
    return str(i) if i not in range(0, 10) else '0' + str(i)


def get_b_id(_):
    i = Block.objects.get(name=_).id
    return str(i) if i not in range(0, 10) else '0' + str(i)