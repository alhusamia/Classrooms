# Generated by Django 2.1.5 on 2020-02-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_auto_20200219_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=10),
        ),
    ]
