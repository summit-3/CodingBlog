# Generated by Django 3.1.1 on 2020-09-28 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0002_code_problem_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='problem_description',
            field=models.CharField(max_length=500),
        ),
    ]