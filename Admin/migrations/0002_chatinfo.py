# Generated by Django 2.0.1 on 2020-10-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='chatInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sender', models.CharField(max_length=20)),
                ('receiver', models.CharField(max_length=20)),
                ('status', models.CharField(default='Pending', max_length=20)),
            ],
        ),
    ]
