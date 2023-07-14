# Generated by Django 3.1.3 on 2020-12-02 22:43

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_auto_20201202_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='video',
            field=s3direct.fields.S3DirectField(blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='record_id',
            field=models.CharField(default='UctH4XPb', max_length=8, null=True, unique=True),
        ),
    ]