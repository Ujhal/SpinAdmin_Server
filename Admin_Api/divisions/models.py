from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

class SubDivision(models.Model):
    name = models.CharField(max_length=64, unique=True)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name='district')

    def __str__(self):
        return self.name

    class Meta:
        ordering=('district_id',)


class Block(models.Model):
    name = models.CharField(max_length=64, unique=True)
    subdivision = models.ForeignKey(
        SubDivision, on_delete=models.CASCADE, related_name="subdivision")
    # district = models.ForeignKey(
    #     SubDivision, on_delete=models.CASCADE, to_field='district')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=('subdivision_id',)