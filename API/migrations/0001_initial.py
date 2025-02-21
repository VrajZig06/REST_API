# Generated by Django 5.1.6 on 2025-02-21 04:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StreamPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=70)),
                ('website', models.URLField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('storyline', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField()),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.streamplatform')),
            ],
        ),
    ]
