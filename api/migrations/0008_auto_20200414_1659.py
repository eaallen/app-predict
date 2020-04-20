# Generated by Django 3.0.3 on 2020-04-14 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_airbnb_room_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.TextField(blank=True, null=True)),
                ('size_bytes', models.TextField(blank=True, null=True)),
                ('currency', models.TextField(blank=True, null=True)),
                ('price', models.TextField(blank=True, null=True)),
                ('rating_count_tot', models.TextField(blank=True, null=True)),
                ('rating_count_ver', models.TextField(blank=True, null=True)),
                ('user_rating', models.TextField(blank=True, null=True)),
                ('user_rating_ver', models.TextField(blank=True, null=True)),
                ('ver', models.TextField(blank=True, null=True)),
                ('cont_rating', models.TextField(blank=True, null=True)),
                ('prime_genre', models.TextField(blank=True, null=True)),
                ('sup_devices_num', models.TextField(blank=True, null=True)),
                ('ipadSc_urls_num', models.TextField(blank=True, null=True)),
                ('lang_num', models.TextField(blank=True, null=True)),
                ('vpp_lic', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AirBnb',
        ),
    ]