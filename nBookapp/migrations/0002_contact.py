# Generated by Django 3.2.7 on 2021-11-14 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nBookapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
            ],
        ),
    ]
