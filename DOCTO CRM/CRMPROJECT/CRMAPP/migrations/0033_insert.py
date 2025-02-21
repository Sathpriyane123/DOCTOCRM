# Generated by Django 3.2.24 on 2024-02-13 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRMAPP', '0032_delete_insert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('leads', 'Leads'), ('follow up', 'Follow up'), ('closable', 'Closable')], max_length=100)),
                ('priority', models.CharField(choices=[('hot', 'Hot'), ('average', 'Average'), ('low', 'Low')], max_length=100)),
                ('demodate_and_time', models.DateTimeField()),
                ('producttype', models.CharField(choices=[('select work', 'Select work'), ('online', 'Online'), ('offline', 'Offline'), ('both', 'BOTH'), ('digital marketing + website', 'Digital Markecting + website')], max_length=100)),
                ('description', models.TextField(max_length=10000)),
                ('did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRMAPP.doctor2')),
            ],
        ),
    ]
