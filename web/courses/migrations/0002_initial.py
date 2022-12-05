# Generated by Django 4.1.2 on 2022-10-28 12:49

import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("courses", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="studentenrollment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="problemset",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="problem_sets",
                to="courses.course",
            ),
        ),
        migrations.AddField(
            model_name="problemset",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AddField(
            model_name="coursegroup",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="groups",
                to="courses.course",
            ),
        ),
        migrations.AddField(
            model_name="coursegroup",
            name="students",
            field=models.ManyToManyField(
                blank=True, related_name="course_groups", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="institution",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="institution",
                to="courses.institution",
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="students",
            field=models.ManyToManyField(
                blank=True,
                related_name="courses",
                through="courses.StudentEnrollment",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="teachers",
            field=models.ManyToManyField(
                blank=True, related_name="taught_courses", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterUniqueTogether(
            name="studentenrollment",
            unique_together={("course", "user")},
        ),
        migrations.AlterOrderWithRespectTo(
            name="problemset",
            order_with_respect_to="course",
        ),
    ]