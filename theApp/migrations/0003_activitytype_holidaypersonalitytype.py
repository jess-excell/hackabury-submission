# Generated by Django 5.2.1 on 2025-05-31 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0002_alter_addon_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('image_src', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='HolidayPersonalityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('image_src', models.CharField()),
                ('recommended_activities', models.ManyToManyField(to='theApp.activitytype')),
            ],
        ),
    ]
