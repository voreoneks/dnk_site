# Generated by Django 3.2.5 on 2021-11-18 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0029_auto_20211110_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на материал'),
        ),
    ]