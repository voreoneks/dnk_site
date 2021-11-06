# Generated by Django 3.2.5 on 2021-11-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0031_alter_maininfodocs_release_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfodocs',
            name='phone_number',
            field=models.CharField(max_length=12, verbose_name='Телефон для связи'),
        ),
        migrations.AlterField(
            model_name='maininfodocs',
            name='release_type',
            field=models.CharField(choices=[('SINGLE', 'Сингл'), ('CLIP', 'Видеоклип'), ('ALBUM', 'Альбом / ЕР')], default='SINGLE', max_length=15, null=True, verbose_name='Тип релиза'),
        ),
    ]
