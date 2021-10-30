# Generated by Django 3.2.5 on 2021-10-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0017_alter_maininfo_is_update_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfo',
            name='is_update_photo',
            field=models.CharField(choices=[('NO', 'Нет'), ('YES', 'Да')], default='NO', max_length=4, verbose_name='Необходимо ли обновить/добавить фото в карточках артиста на площадках?'),
        ),
    ]