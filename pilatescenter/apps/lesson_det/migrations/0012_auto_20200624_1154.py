# Generated by Django 3.0.7 on 2020-06-24 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_det', '0011_auto_20200624_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson_det',
            name='hour_chance',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lesson_det',
            name='hour_end',
            field=models.TimeField(blank=True, null=True),
        ),
    ]