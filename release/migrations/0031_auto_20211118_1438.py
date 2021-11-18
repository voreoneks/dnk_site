# Generated by Django 3.2.5 on 2021-11-18 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0030_alter_audio_audio_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='genre',
            field=models.CharField(choices=[('NONE', 'Не выбрано'), ('BLUES', 'BLUES'), ('CHILDREN`S', 'CHILDREN`S'), ('CHRISTIAN', 'CHRISTIAN'), ('CLASSICAL', 'CLASSICAL'), ('COUNTRY', 'COUNTRY'), ('EDUCATIONAL', 'EDUCATIONAL'), ('ELECTRONIC', 'ELECTRONIC'), ('FOLK', 'FOLK'), ('HIP-HOP/RAP', 'HIP-HOP/RAP'), ('HOLIDAY', 'HOLIDAY'), ('JAZZ', 'JAZZ'), ('LATIN MUSIC', 'LATIN MUSIC'), ('METAL', 'METAL'), ('NEW AGE', 'NEW AGE'), ('POP', 'POP'), ('ALTERNATIVE', 'ALTERNATIVE'), ('R&B', 'R&B'), ('ROCK', 'ROCK'), ('PUNK', 'PUNK'), ('WORLD MUSIC', 'WORLD MUSIC')], default='NONE', max_length=25, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='lexis',
            field=models.CharField(choices=[('NONE', 'Не выбрано'), ('NO', 'Отсутствует'), ('YES', 'Присутствует')], default='NONE', max_length=25, verbose_name='Ненормативная лексика в песне'),
        ),
    ]