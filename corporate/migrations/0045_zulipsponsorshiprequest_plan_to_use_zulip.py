# Generated by Django 5.0.10 on 2025-01-14 17:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("corporate", "0001_squashed_0044_convert_ids_to_bigints"),
    ]

    operations = [
        migrations.AddField(
            model_name="zulipsponsorshiprequest",
            name="plan_to_use_zulip",
            field=models.TextField(default=""),
        ),
    ]
