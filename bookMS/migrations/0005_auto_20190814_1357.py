# Generated by Django 2.2.4 on 2019-08-14 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMS', '0004_auto_20190814_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='borrows',
            name='borrow_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='borrows',
            name='return_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='user_sex',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='books',
            name='user_state',
            field=models.IntegerField(default=0),
        ),
    ]
