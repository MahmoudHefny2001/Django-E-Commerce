# Generated by Django 4.2.5 on 2024-03-23 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='../utils/black.jpg', null=True, upload_to='images/customers/profiles/')),
                ('bio', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Customer Profile',
                'verbose_name_plural': 'Customer Profiles',
                'db_table': 'customer_profiles',
            },
        ),
    ]
