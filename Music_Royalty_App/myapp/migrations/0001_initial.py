# Generated by Django 3.2.6 on 2021-12-16 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Altafonte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_Id', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('artist', models.CharField(blank=True, max_length=20, null=True)),
                ('track', models.CharField(blank=True, max_length=100, null=True)),
                ('net', models.FloatField(blank=True, default=0.0, null=True)),
                ('count', models.CharField(blank=True, max_length=20, null=True)),
                ('ret', models.FloatField(blank=True, default=0.0, null=True)),
                ('cambio', models.FloatField(blank=True, default=0.0, null=True)),
                ('altafonte_aoa', models.FloatField(blank=True, default=0.0, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('admin_approval', models.BooleanField(default=False)),
            ],
        ),
    ]