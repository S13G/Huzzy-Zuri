# Generated by Django 4.1 on 2022-08-10 23:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_school_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='NIN',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.MinLengthValidator(11)]),
        ),
    ]
