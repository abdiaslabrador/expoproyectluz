# Generated by Django 3.0.4 on 2020-04-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_user', '0006_auto_20200410_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=255, null=True, unique=True),
        ),
    ]
