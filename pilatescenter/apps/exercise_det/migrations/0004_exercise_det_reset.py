# Generated by Django 3.0.7 on 2020-06-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_det', '0003_auto_20200421_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise_det',
            name='reset',
            field=models.BooleanField(default=True),
        ),
    ]
