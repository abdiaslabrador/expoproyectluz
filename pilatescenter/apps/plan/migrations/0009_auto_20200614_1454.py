# Generated by Django 3.0.7 on 2020-06-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0008_auto_20200614_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
