# Generated by Django 4.2.1 on 2023-06-01 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0003_bookmark_like_reply"),
    ]

    operations = [
        migrations.RemoveField(model_name="reply", name="is_like",),
        migrations.AddField(
            model_name="reply",
            name="reply_content",
            field=models.TextField(default=""),
        ),
    ]
