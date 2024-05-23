# Generated by Django 3.2.23 on 2024-02-06 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRMAPP', '0008_delete_doctor1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calllater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nextcalling', models.DateTimeField(max_length=10)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Followup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nextfollowup', models.DateTimeField(max_length=10)),
                ('description', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Insert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('leads', 'Leads'), ('follow up', 'Follow up'), ('closable', 'Closable')], max_length=100)),
                ('priority', models.CharField(choices=[('hot', 'Hot'), ('average', 'Average'), ('low', 'Low')], max_length=100)),
                ('demodate_and_time', models.DateTimeField()),
                ('producttype', models.CharField(choices=[('select work', 'Select work'), ('online', 'Online'), ('offline', 'Offline'), ('both', 'BOTH'), ('digital marketing + website', 'Digital Markecting + website')], max_length=100)),
                ('description', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Notintrested',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(max_length=10)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Rnr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nextcalling', models.DateTimeField(max_length=10)),
            ],
        ),
    ]