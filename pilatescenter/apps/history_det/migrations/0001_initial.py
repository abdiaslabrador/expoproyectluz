# Generated by Django 3.0.7 on 2020-07-03 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercise', '0013_auto_20200627_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='history_det',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_max', models.IntegerField(blank=True, default=0, null=True)),
                ('cant_in', models.IntegerField(default=0)),
                ('quota', models.IntegerField(default=0)),
                ('day_lesson', models.DateField(blank=True, null=True)),
                ('hour_chance', models.TimeField(blank=True, null=True)),
                ('hour_lesson', models.TimeField(blank=True, null=True)),
                ('hour_end', models.TimeField(blank=True, null=True)),
                ('id_exercise_fk', models.ForeignKey(blank=True, db_column='id_exercise_fk', null=True, on_delete=django.db.models.deletion.CASCADE, to='exercise.Exercise')),
                ('id_user_fk', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]