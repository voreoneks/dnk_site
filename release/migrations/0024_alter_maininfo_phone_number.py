# Generated by Django 3.2.5 on 2021-11-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0023_alter_audio_timing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfo',
            name='phone_number',
            field=models.CharField(max_length=12, verbose_name='Телефон'),
        ),
    ]