# Generated by Django 2.0.6 on 2018-06-24 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constructed',
            name='created_date',
        ),
    ]