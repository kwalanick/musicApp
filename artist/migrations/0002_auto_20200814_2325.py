# Generated by Django 3.1 on 2020-08-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
