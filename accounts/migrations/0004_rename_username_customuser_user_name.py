# Generated by Django 4.1 on 2022-11-06 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='username',
            new_name='user_name',
        ),
    ]
