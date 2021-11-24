# Generated by Django 3.2.4 on 2021-10-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_name',
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=50, null=True),
        ),
    ]