from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

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

class Donation(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    categories = models.ManyToManyField(Category, verbose_name='Categories')
    institution  = models.ForeignKey('Institution', verbose_name='Institution', on_delete=models.CASCADE)
    address = models.CharField(max_length=200, verbose_name='Address',)
    phone_number = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Phone')
    city = models.CharField(max_length=100, verbose_name='City')
    zip_code = models.CharField( max_length=5, default="45000", verbose_name='Zip code')
    pick_up_date = models.DateField(verbose_name='Date pick up', default=timezone.now)
    pick_up_time = models.DateTimeField(auto_now=True, verbose_name='Time pick up')
    pick_up_comment = models.TextField(verbose_name='Comment', null=True, blank=True)
    user = models.ForeignKey(User, null=True, verbose_name='User', on_delete=models.CASCADE)
