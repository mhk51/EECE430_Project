# Generated by Django 3.2.9 on 2021-12-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nBookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.CharField(default='', max_length=40),
        ),
    ]