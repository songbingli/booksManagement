# Generated by Django 2.2.4 on 2019-08-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMS', '0006_auto_20190814_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrows',
            name='return_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
