# Generated by Django 4.0.6 on 2022-11-16 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='store',
            options={'ordering': ['-created_at'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
