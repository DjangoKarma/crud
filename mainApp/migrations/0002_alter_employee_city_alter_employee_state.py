# Generated by Django 4.2 on 2023-05-04 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="city",
            field=models.CharField(blank=True, default="", max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="state",
            field=models.CharField(blank=True, default="", max_length=60, null=True),
        ),
    ]
