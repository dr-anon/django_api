# Generated by Django 4.2.7 on 2023-11-15 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('hair_color', models.CharField(max_length=20)),
            ],
        ),
    ]
