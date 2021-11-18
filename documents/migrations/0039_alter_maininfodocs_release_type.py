# Generated by Django 3.2.5 on 2021-11-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0038_alter_maininfodocs_release_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfodocs',
            name='release_type',
            field=models.CharField(choices=[('ALBUM', 'Альбом / ЕР'), ('SINGLE', 'Сингл'), ('CLIP', 'Видеоклип')], default='SINGLE', max_length=15, null=True, verbose_name='Тип релиза'),
        ),
    ]
