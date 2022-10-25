import os
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = ('Categories')


class Product(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('Products', new_filename)

    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = ('Products')
        index_together = (('id', 'slug'),)

class Promo(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('Promo', new_filename)

    period = (
        ('month', 'month'),
        ('week', 'week'),
        ('day', 'day'),
    )

    type = models.CharField(max_length=50, null=False, choices=period)
    promo_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, db_index=True)
    description = models.CharField(max_length=500)
    sale_value = models.PositiveSmallIntegerField(validators=[MinValueValidator(2), MaxValueValidator(99)])
    end_of_promo = models.DateTimeField()
    photo = models.ImageField(upload_to=get_file_name)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = ('Promo')


