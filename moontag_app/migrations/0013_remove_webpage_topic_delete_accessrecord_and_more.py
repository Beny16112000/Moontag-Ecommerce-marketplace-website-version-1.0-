# Generated by Django 4.0.6 on 2022-08-07 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moontag_app', '0012_alter_brand_img_alter_category_img_alter_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='topic',
        ),
        migrations.DeleteModel(
            name='AccessRecord',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='Webpage',
        ),
    ]
