# Generated by Django 3.0.7 on 2020-12-31 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_systempilates_cant_max'),
    ]

    operations = [
        migrations.AddField(
            model_name='systempilates',
            name='documentation',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]