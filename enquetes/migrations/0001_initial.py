# Generated by Django 3.1.1 on 2020-09-05 16:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=50)),
                ('data_publicacao', models.DateField(default=datetime.date(2020, 9, 5))),
            ],
        ),
    ]