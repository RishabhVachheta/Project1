# Generated by Django 4.2.4 on 2023-08-03 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='productimage'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='productimage'),
        ),
    ]
