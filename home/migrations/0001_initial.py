# Generated by Django 3.1.3 on 2020-12-05 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('tid', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('show', models.CharField(max_length=20)),
                ('tier', models.CharField(max_length=10)),
                ('attendees', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
