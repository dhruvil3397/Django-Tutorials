# Generated by Django 3.2.8 on 2021-10-11 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='thumbnail',
        ),
    ]
