# Generated by Django 5.0.1 on 2024-01-09 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0011_remove_item_prod_code_alter_cusorders_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cusorders',
            name='prod_code',
        ),
    ]