# Generated by Django 4.0.6 on 2022-10-11 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_category_order_alter_product_id_order_det_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
