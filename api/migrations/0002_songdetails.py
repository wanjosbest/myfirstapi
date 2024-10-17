# Generated by Django 5.1.2 on 2024-10-16 22:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='songdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Song', models.FileField(null=True, upload_to='songs')),
                ('Title', models.CharField(max_length=100, null=True, unique=True)),
                ('Featuredimage', models.ImageField(null=True, upload_to='images')),
                ('Description', models.TextField(max_length=5000, null=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
        ),
    ]