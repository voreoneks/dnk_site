# Generated by Django 3.2.5 on 2021-10-31 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0023_alter_maininfomarketing_release_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfomarketing',
            name='release_type',
            field=models.CharField(choices=[('SINGLE', 'Сингл'), ('MAXI_SINGLE', 'Максисингл'), ('ALBUM', 'Альбом / ЕР'), ('CLIP', 'Видеоклип')], default='SINGLE', max_length=20, verbose_name='Тип релиза'),
        ),
        migrations.AlterField(
            model_name='maininfomarketing',
            name='youtube',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='YouTube'),
        ),
    ]
