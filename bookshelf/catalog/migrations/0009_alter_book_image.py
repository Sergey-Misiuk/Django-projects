# Generated by Django 4.2.1 on 2023-06-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='Фото'),
        ),
    ]
