# Generated by Django 4.1 on 2022-11-18 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0005_comment_post"),
    ]

    operations = [
        migrations.CreateModel(
            name="userInfo",
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
                ("username", models.CharField(max_length=10)),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("email_id", models.EmailField(max_length=254)),
                ("phone_no", models.CharField(max_length=10)),
                (
                    "gender",
                    models.CharField(
                        choices=[("0", "female"), ("1", "male")],
                        default="0",
                        max_length=20,
                    ),
                ),
                ("password", models.CharField(max_length=10)),
            ],
            options={"ordering": ("username",),},
        ),
        migrations.RemoveField(model_name="post", name="comments",),
        migrations.RemoveField(model_name="post", name="username",),
        migrations.DeleteModel(name="comment",),
        migrations.DeleteModel(name="Post",),
        migrations.DeleteModel(name="User",),
    ]
