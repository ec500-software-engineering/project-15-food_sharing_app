# Generated by Django 2.1.2 on 2019-04-25 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_restaurantprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='halal',
        ),
        migrations.RemoveField(
            model_name='food',
            name='kosher',
        ),
    ]
