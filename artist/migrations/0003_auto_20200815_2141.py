# Generated by Django 3.1 on 2020-08-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20200814_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]