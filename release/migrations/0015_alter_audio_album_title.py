# Generated by Django 3.2.5 on 2021-10-20 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0014_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='album_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название альбома'),
        ),
    ]
