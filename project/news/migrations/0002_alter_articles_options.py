# Generated by Django 4.2.5 on 2023-09-21 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
