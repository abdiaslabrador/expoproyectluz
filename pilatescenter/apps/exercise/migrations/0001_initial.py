# Generated by Django 3.0.4 on 2020-04-21 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('total_days', models.IntegerField(default=0)),
                ('oportunities', models.IntegerField(default=0)),
            ],
        ),
    ]
