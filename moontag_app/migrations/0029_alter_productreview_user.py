# Generated by Django 4.0.6 on 2022-10-30 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moontag_app', '0028_alter_productreview_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='user',
            field=models.CharField(editable=False, max_length=100),
        ),
    ]