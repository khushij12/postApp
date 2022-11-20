# Generated by Django 4.1 on 2022-11-20 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "registration",
            "0006_userinfo_remove_post_comments_remove_post_username_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=50)),
                ("phone_number", models.CharField(max_length=10)),
                ("birth_date", models.DateField()),
                ("email", models.EmailField(max_length=254)),
                ("username", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=50)),
                ("password2", models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(name="userInfo",),
    ]
