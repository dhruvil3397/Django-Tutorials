# Generated by Django 3.2.6 on 2021-12-17 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kisom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(blank=True, max_length=20, null=True)),
                ('content_name', models.CharField(blank=True, max_length=100, null=True)),
                ('net_royalty_total', models.FloatField(blank=True, default=0.0, null=True)),
                ('count', models.CharField(blank=True, max_length=20, null=True)),
                ('ret', models.FloatField(blank=True, default=0.0, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('admin_approval', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rbt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(blank=True, max_length=20, null=True)),
                ('content_name', models.CharField(blank=True, max_length=100, null=True)),
                ('rev_x_2', models.FloatField(blank=True, default=0.0, null=True)),
                ('count', models.CharField(blank=True, max_length=20, null=True)),
                ('ret', models.FloatField(blank=True, default=0.0, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('admin_approval', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
