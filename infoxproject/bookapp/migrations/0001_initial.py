# Generated by Django 3.2.13 on 2022-05-31 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=150)),
                ('desc', models.TextField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
