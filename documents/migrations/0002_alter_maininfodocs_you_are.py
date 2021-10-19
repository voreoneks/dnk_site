# Generated by Django 3.2.5 on 2021-10-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfodocs',
            name='you_are',
            field=models.CharField(choices=[('IPRF', 'ИП РФ'), ('IPIN', 'ИП Иностранный'), ('SAM', 'Самозанятый'), ('OOO', 'ООО')], default='IPRF', max_length=20, verbose_name='Вы являетесь'),
        ),
    ]