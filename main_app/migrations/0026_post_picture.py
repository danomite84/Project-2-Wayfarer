# Generated by Django 3.1.2 on 2020-11-05 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0025_auto_20201105_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
