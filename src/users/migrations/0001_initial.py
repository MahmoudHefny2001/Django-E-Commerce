# Generated by Django 4.2.5 on 2024-03-23 23:13

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('role', models.CharField(blank=True, choices=[('CUSTOMER', 'Customer'), ('ADMIN', 'Admin'), ('MERCHANT', 'Merchant')], default='CUSTOMER', max_length=50, null=True)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=254, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('phone_number', models.CharField(blank=True, db_index=True, max_length=20, null=True, unique=True, validators=[users.validators.valid_phone_number])),
                ('is_superuser', models.BooleanField(blank=True, default=False, null=True)),
                ('is_staff', models.BooleanField(blank=True, default=False, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
