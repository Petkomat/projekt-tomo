# Generated by Django 4.1.2 on 2023-12-20 06:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0003_alter_coursegroup_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="library",
            field=models.BooleanField(default=False),
        ),
    ]