# Generated by Django 3.1.7 on 2021-03-11 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0004_auto_20210310_0850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='created',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='updated',
        ),
    ]
