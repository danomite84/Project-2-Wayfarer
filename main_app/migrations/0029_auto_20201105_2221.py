# Generated by Django 3.1.3 on 2020-11-06 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0028_merge_20201105_1617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['-id']},
        ),
    ]