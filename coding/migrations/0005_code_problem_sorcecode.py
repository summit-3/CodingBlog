# Generated by Django 3.1.1 on 2020-09-28 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0004_auto_20200928_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='problem_sorceCode',
            field=models.CharField(default=True, max_length=5000),
        ),
    ]
