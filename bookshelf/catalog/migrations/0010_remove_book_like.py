# Generated by Django 4.2.1 on 2023-06-11 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='like',
        ),
    ]