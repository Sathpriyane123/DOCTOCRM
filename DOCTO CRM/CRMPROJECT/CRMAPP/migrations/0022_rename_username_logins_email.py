# Generated by Django 3.2.24 on 2024-02-09 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRMAPP', '0021_rename_user_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logins',
            old_name='username',
            new_name='email',
        ),
    ]