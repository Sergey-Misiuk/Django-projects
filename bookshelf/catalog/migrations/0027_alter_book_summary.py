# Generated by Django 4.2.1 on 2023-06-16 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0026_alter_book_image_alter_book_pdf_file_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(max_length=100, verbose_name='Описание'),
        ),
    ]
