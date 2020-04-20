# Generated by Django 3.0.3 on 2020-03-25 11:54

import api.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='address2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='items',
            field=api.fields.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='sale',
            name='payment_intent',
            field=api.fields.JSONField(default=dict),
        ),
    ]