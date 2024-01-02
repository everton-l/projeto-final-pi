# Generated by Django 4.2.2 on 2023-12-14 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_remove_flores_bioma"),
    ]

    operations = [
        migrations.AddField(
            model_name="flores",
            name="bioma",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.bioma",
            ),
        ),
    ]