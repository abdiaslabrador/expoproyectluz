# Generated by Django 3.0.7 on 2020-06-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_auto_20200616_1625'),
        ('lesson_det', '0003_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='id_exercise_fk',
            field=models.ManyToManyField(to='exercise.Exercise'),
        ),
    ]
