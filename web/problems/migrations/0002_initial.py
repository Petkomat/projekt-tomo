# Generated by Django 4.1.2 on 2022-10-28 12:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("courses", "0001_initial"),
        ("problems", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalproblem",
            name="history_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="historicalproblem",
            name="problem_set",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="courses.problemset",
            ),
        ),
        migrations.AddField(
            model_name="historicalpart",
            name="history_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="historicalpart",
            name="problem",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="problems.problem",
            ),
        ),
        migrations.AlterOrderWithRespectTo(
            name="problem",
            order_with_respect_to="problem_set",
        ),
        migrations.AlterOrderWithRespectTo(
            name="part",
            order_with_respect_to="problem",
        ),
    ]