# Generated by Django 3.2.5 on 2021-11-18 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0039_alter_maininfomarketing_release_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfomarketing',
            name='release_type',
            field=models.CharField(choices=[('MAXI_SINGLE', 'Максисингл'), ('ALBUM', 'Альбом / ЕР'), ('CLIP', 'Видеоклип'), ('SINGLE', 'Сингл')], default='SINGLE', max_length=20, verbose_name='Тип релиза'),
        ),
    ]
