# Generated by Django 2.1.2 on 2019-04-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20190425_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantprofile',
            name='email',
            field=models.CharField(blank=True, max_length=265),
        ),
    ]