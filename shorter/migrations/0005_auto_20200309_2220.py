# Generated by Django 3.0.3 on 2020-03-09 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0004_auto_20200308_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(max_length=1000),
        ),
    ]
