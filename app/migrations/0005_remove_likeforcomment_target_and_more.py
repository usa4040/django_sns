# Generated by Django 4.1 on 2022-11-19 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20221117_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likeforcomment',
            name='target',
        ),
        migrations.RemoveField(
            model_name='likeforcomment',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='LikeForComment',
        ),
    ]
