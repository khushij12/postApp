# Generated by Django 4.1 on 2022-11-18 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0004_user_delete_userinfo"),
    ]

    operations = [
        migrations.CreateModel(
            name="comment",
            fields=[
                (
                    "username",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="registration.user",
                    ),
                ),
                ("comts", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "username",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="registration.user",
                    ),
                ),
                ("caption", models.TextField()),
                ("post", models.ImageField(upload_to="Images/")),
                ("like", models.IntegerField()),
                ("comments", models.ManyToManyField(to="registration.comment")),
            ],
            options={"verbose_name_plural": "All Post",},
        ),
    ]
