# Generated by Django 4.0 on 2022-05-15 11:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_story_story_length_custom_alter_story_story_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='story_length',
            field=models.IntegerField(choices=[(5, '5'), (10, '10'), (15, '15'), (20, ' 20'), (0, 'custom')], null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_length_custom',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(60)]),
        ),
    ]