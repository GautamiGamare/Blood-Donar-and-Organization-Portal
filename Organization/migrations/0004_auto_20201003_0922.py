# Generated by Django 2.0.1 on 2020-10-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0003_auto_20200926_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationmodel',
            name='email',
            field=models.EmailField(max_length=40, unique=True),
        ),
    ]
