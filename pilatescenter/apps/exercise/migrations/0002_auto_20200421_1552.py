# Generated by Django 3.0.4 on 2020-04-21 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='oportunities',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='total_days',
        ),
    ]
