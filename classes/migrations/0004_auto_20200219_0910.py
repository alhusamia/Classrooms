# Generated by Django 2.1.5 on 2020-02-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('m', 'Female')], default=None, max_length=10),
        ),
    ]
