# Generated by Django 4.2.9 on 2024-02-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edible_products', '0007_alter_edibleproduct_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productweightprice',
            name='weight',
            field=models.IntegerField(help_text='Weight in grams'),
        ),
    ]
