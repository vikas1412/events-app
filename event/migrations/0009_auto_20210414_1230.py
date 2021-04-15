# Generated by Django 3.2 on 2021-04-14 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_event_all_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='day',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='month',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='year',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]