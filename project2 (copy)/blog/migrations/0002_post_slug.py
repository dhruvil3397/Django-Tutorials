# Generated by Django 3.2.8 on 2021-10-11 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]
