# Generated by Django 2.0 on 2019-09-04 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empid', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
