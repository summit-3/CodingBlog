# Generated by Django 3.1.1 on 2020-09-30 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0011_code_problem_numbeer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programming_facts', models.TextField(max_length=5000)),
            ],
        ),
    ]
