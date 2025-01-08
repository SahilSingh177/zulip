# Generated by Django 5.0.9 on 2024-12-17 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0652_remove_realm_invite_to_stream_policy"),
    ]

    operations = [
        migrations.AddField(
            model_name="stream",
            name="can_add_subscribers_group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="+",
                to="zerver.usergroup",
            ),
        ),
    ]