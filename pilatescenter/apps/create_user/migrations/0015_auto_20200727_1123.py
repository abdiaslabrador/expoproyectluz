# Generated by Django 3.0.7 on 2020-07-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_user', '0014_customuser_is_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]