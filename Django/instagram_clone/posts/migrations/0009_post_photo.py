# Generated by Django 4.0 on 2022-04-14 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_commentlikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
