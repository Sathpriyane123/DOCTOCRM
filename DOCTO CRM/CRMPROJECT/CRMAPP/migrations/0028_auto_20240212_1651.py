# Generated by Django 3.2.24 on 2024-02-12 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRMAPP', '0027_auto_20240212_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newstaff',
            old_name='defaultlanguage',
            new_name='Defaultlanguage',
        ),
        migrations.RenameField(
            model_name='newstaff',
            old_name='defaultstate',
            new_name='Defaultstate',
        ),
        migrations.RenameField(
            model_name='newstaff',
            old_name='direction',
            new_name='Direction',
        ),
        migrations.RenameField(
            model_name='newstaff',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='newstaff',
            old_name='emailsig',
            new_name='Emailsig',
        ),
        migrations.RenameField(
            model_name='newstaff',
            old_name='facebook',
            new_name='Facebook',
        ),
        migrations.RenameField(
            model_name='newstaff',
            old_name='hourlyrate',
            new_name='Hourlyrate',
        ),
        migrations.RenameField(
            model_name='newstaff',
            old_name='lastname',
            new_name='Lastname',
        ),
        migrations.RenameField(
            model_name='newstaff',
            old_name='linkedin',
            new_name='Linkedin',
        ),
        migrations.RenameField(
            model_name='newstaff',
            old_name='password',
            new_name='Password',
        ),
        migrations.RenameField(
            model_name='newstaff',
            old_name='phoneno',
            new_name='Phoneno',
        ),
        migrations.RenameField(
            model_name='newstaff',
            old_name='skype',
            new_name='Skype',
        ),
    ]
