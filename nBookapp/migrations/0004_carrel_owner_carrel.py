# Generated by Django 3.2.9 on 2021-12-02 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nBookapp', '0003_alter_book_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrel',
            name='owner_Carrel',
            field=models.CharField(default='No Owner', max_length=30),
        ),
    ]