# Generated by Django 3.2.5 on 2021-11-09 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0033_auto_20211109_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfodocs',
            name='release_type',
            field=models.CharField(choices=[('ALBUM', 'Альбом / ЕР'), ('CLIP', 'Видеоклип'), ('SINGLE', 'Сингл')], default='SINGLE', max_length=15, null=True, verbose_name='Тип релиза'),
        ),
    ]
