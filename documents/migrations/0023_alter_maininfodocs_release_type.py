# Generated by Django 3.2.5 on 2021-10-31 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0022_auto_20211030_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfodocs',
            name='release_type',
            field=models.CharField(choices=[('CLIP', 'Видеоклип'), ('SINGLE', 'Сингл'), ('ALBUM', 'Альбом / ЕР')], default='SINGLE', max_length=15, null=True, verbose_name='Тип релиза'),
        ),
    ]
