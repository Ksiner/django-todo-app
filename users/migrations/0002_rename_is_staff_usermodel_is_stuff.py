# Generated by Django 4.1.7 on 2023-03-18 09:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usermodel",
            old_name="is_staff",
            new_name="is_stuff",
        ),
    ]
