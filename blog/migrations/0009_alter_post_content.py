# Generated by Django 3.2.4 on 2021-10-02 06:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20211001_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(800)]),
        ),
    ]
