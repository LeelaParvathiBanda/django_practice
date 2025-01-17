# Generated by Django 5.1.4 on 2024-12-07 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='playerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(blank=True, max_length=50)),
                ('ptname', models.CharField(blank=True, max_length=50)),
                ('is_captain', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TeamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
