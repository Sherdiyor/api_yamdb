# Generated by Django 3.2 on 2024-03-25 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_alter_user_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'verbose_name': 'Произведения', 'verbose_name_plural': 'Произведения'},
        ),
    ]
