# Generated by Django 4.0 on 2022-05-12 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_story_story_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='story_length',
            field=models.IntegerField(choices=[(5, '5'), (10, '10'), (15, '15'), (20, ' 20')], null=True),
        ),
    ]