# Generated by Django 5.0.3 on 2024-03-13 16:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zomato", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="sentiments",
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="summaries",
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="url",
            field=models.URLField(max_length=1000),
        ),
    ]
