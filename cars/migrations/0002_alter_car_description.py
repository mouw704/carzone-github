# Generated by Django 4.2.6 on 2023-10-15 18:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
