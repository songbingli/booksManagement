# Generated by Django 2.2.4 on 2019-08-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMS', '0010_auto_20190815_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_sn',
            field=models.BigIntegerField(),
        ),
    ]
