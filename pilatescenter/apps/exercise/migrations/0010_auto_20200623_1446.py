# Generated by Django 3.0.7 on 2020-06-23 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0009_auto_20200623_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=28, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='hour',
            name='id_day_fk',
            field=models.ForeignKey(blank=True, db_column='id_day_fk', null=True, on_delete=django.db.models.deletion.CASCADE, to='exercise.Day'),
        ),
    ]
