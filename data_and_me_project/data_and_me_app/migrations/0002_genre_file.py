# Generated by Django 2.2.7 on 2019-11-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_and_me_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='file',
            field=models.FileField(blank=True, upload_to='file'),
        ),
    ]