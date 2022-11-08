import os
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField
from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse


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
        return os.path.join('products', new_filename)

    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(max_length=50, unique=True)
    description = RichTextField(max_length=500)
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

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.id, self.slug])


class Promo(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('promo', new_filename)

    period = (
        ('month', 'month'),
        ('week', 'week'),
        ('day', 'day'),
    )

    type = models.CharField(max_length=50, null=False, choices=period)
    promo_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, db_index=True)
    description = RichTextField(max_length=500)
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


class Testimonials(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('testimonials', new_filename)

    name = models.CharField(max_length=100, unique=True)
    profession = models.CharField(max_length=50)
    review = models.TextField(max_length=300)
    position = models.SmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f'{self.name}'


class About(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('about', new_filename)

    title_line_1 = models.CharField(max_length=50, blank=True, db_index=True)
    title_line_2 = models.CharField(max_length=50, blank=True, db_index=True)
    paragraph_1 = models.TextField(max_length=500, blank=True, db_index=True)
    paragraph_2 = models.TextField(max_length=500, blank=True, db_index=True)
    video_link = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=get_file_name)

    class Meta:
        verbose_name_plural = 'About section'

    def __str__(self):
        return f'About'


class WhyUs(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('whyus', new_filename)

    delivery_title = models.CharField(max_length=50)
    delivery_text = models.TextField(max_length=200)
    price_title = models.CharField(max_length=50)
    price_text = models.TextField(max_length=200)
    service_title = models.CharField(max_length=50)
    service_text = models.TextField(max_length=200)
    refund_title = models.CharField(max_length=50)
    refund_text = models.TextField(max_length=200)
    photo = models.ImageField(upload_to=get_file_name)

    class Meta:
        verbose_name_plural = 'WhyUs'

    def __str__(self):
        return f'WhyUs'


class Partners(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('partners_logos', new_filename)

    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=get_file_name, )
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Partners logos'

    def __str__(self):
        return f'{self.name}'


class Banner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('Banner', new_filename)

    name = models.CharField(max_length=50)
    banner_image = models.ImageField(upload_to=get_file_name, help_text='Recommended resolution: 1920x494px' )
    is_visible = models.BooleanField(default=True, )

    class Meta:
        verbose_name_plural = 'Banner'

    def __str__(self):
        return f'{self.name}'


class Info(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('main', new_filename)

    brand_name = models.CharField(max_length=50, db_index=True)
    brand_logo = models.ImageField(upload_to=get_file_name)
    main_title_line_1 = models.CharField(max_length=200, db_index=True)
    main_title_line_2 = models.CharField(max_length=200, db_index=True)
    about_title_line_1 = models.CharField(max_length=200, db_index=True)
    about_title_line_2 = models.CharField(max_length=200, db_index=True)
    contact_title_line_1 = models.CharField(max_length=200, db_index=True)
    contact_title_line_2 = models.CharField(max_length=200, db_index=True)
    shop_title_line_1 = models.CharField(max_length=200, db_index=True)
    shop_title_line_2 = models.CharField(max_length=200, db_index=True)
    our_team_title = models.TextField(max_length=200)
    related_prod_title = models.TextField(max_length=200)


    class Meta:
        verbose_name_plural = 'Main information'

    def __str__(self):
        return f'Main information'


class Contacts(models.Model):
    text = RichTextField(max_length=500)
    address = RichTextField(max_length=500)
    open_hours = RichTextField(max_length=1000)
    contact = RichTextField(max_length=500)
    about_short = models.TextField(max_length=300)
    subscribe_text = models.TextField(max_length=200)
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'Contacts'

class UserMessage(models.Model):
    name = models.CharField(max_length=50)
    phone_re = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message= 'Please enter phone number in format +xxx xx xxx xx xx')
    phone = models.CharField(max_length=15, validators=[phone_re])
    email = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)
    is_processed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date', '-is_processed')

    def __str__(self):
        return f'{self.name} - {self.subject}'