# Generated by Django 3.0.7 on 2020-06-21 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_auto_20200616_1625'),
        ('lesson_det', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson_det',
            name='id_hour_fk',
        ),
        migrations.AddField(
            model_name='hour',
            name='id_exercise_fk',
            field=models.ForeignKey(blank=True, db_column='id_exercise_fk', null=True, on_delete=django.db.models.deletion.CASCADE, to='exercise.Exercise'),
        ),
        migrations.AddField(
            model_name='lesson_det',
            name='hour_lesson',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hour',
            name='hour_chance',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hour',
            name='hour_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hour',
            name='hour_lesson',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
