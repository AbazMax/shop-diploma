# Generated by Django 4.1.2 on 2022-10-25 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promo',
            name='promo_product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.product'),
            preserve_default=False,
        ),
    ]
