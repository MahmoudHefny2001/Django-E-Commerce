# Generated by Django 4.2.5 on 2024-03-11 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0001_initial'),
        ('products', '0002_initial'),
        ('customers', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='customers.customer'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='carts', to='products.product'),
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('customer', 'product')},
        ),
    ]
