# Generated by Django 2.1.5 on 2020-02-18 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20200218_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('exam_grade', models.IntegerField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Classroom')),
            ],
        ),
    ]
