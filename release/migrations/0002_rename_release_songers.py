from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio',
            old_name='songer',
            new_name='songers',
        ),
    ]