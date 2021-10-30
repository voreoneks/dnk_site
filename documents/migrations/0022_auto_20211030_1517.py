# Generated by Django 3.2.5 on 2021-10-30 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0021_auto_20211030_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfodocs',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Обложка (jpg 3000x3000)'),
        ),
        migrations.AlterField(
            model_name='maininfodocs',
            name='release_type',
            field=models.CharField(choices=[('CLIP', 'Видеоклип'), ('ALBUM', 'Альбом / ЕР'), ('SINGLE', 'Сингл')], default='SINGLE', max_length=15, null=True, verbose_name='Тип релиза'),
        ),
    ]
