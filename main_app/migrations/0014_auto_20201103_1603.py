# Generated by Django 3.1.2 on 2020-11-04 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20201103_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='/images/default-profile-img.png', null=True, upload_to='images/'),
        ),
    ]
