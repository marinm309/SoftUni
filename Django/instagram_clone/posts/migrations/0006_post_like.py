# Generated by Django 4.0 on 2022-04-05 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_like_alter_likes_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.IntegerField(default=0, null=True),
        ),
    ]