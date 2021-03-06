# Generated by Django 2.0.1 on 2020-09-24 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonarModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('contact_number', models.IntegerField()),
                ('contact_number_2', models.IntegerField()),
                ('email', models.EmailField(max_length=40)),
                ('blood_group', models.CharField(max_length=10)),
                ('last_donation_date', models.DateField()),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=20)),
                ('photo', models.ImageField(null=True, upload_to='donar_images/')),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
