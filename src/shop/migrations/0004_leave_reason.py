# Generated by Django 4.0 on 2022-01-13 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='reason',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]