from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Category')

class Institution(models.Model):
    V1 = 'fundation'
    V2 = 'organization'
    V3 = 'collection'

    TYPE_INSTITUTION = (
        (V1, 'fundacja'),
        (V2, 'organizacja pozarządowa'),
        (V3, 'zbiórka lokalna')
    )
    categories = models.ManyToManyField(Category, verbose_name='Categories')
    name = models.CharField(max_length=200, verbose_name='Institution')
    description = models.TextField()
    type = models.CharField(
        max_length=200,
        verbose_name='Type',
        choices=TYPE_INSTITUTION,
        default=V1
    )
