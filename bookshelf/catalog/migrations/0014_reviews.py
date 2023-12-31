# Generated by Django 4.2.1 on 2023-06-12 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0013_delete_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=2000, verbose_name='Комментарий')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='Дата комментария')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_book', to='catalog.book', verbose_name='книга')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
