# Generated by Django 3.0.7 on 2020-06-23 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_det', '0007_auto_20200623_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson_det',
            name='day_lesson',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='lesson_det',
            name='hour_lesson',
            field=models.TimeField(),
        ),
    ]
