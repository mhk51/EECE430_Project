# Generated by Django 3.2.9 on 2021-12-02 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nBookapp', '0005_book_borrowed_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='remainingDays',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='borrowed_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 13, 42, 43, 89485)),
        ),
    ]
