# Generated by Django 2.0.1 on 2020-09-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0002_auto_20200924_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationmodel',
            name='password',
            field=models.CharField(default='password', max_length=30),
        ),
        migrations.AddField(
            model_name='organizationmodel',
            name='uname',
            field=models.CharField(default='uname', max_length=30),
        ),
    ]
