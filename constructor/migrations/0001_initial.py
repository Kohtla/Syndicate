# Generated by Django 2.0.6 on 2018-06-24 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Constructed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('chest', models.FloatField()),
                ('height', models.FloatField()),
                ('neck', models.FloatField()),
                ('sleeves', models.FloatField()),
                ('shoulder', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PartsInPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
                ('s', models.FloatField()),
                ('qx', models.FloatField()),
                ('qy', models.FloatField()),
                ('qz', models.FloatField()),
                ('qw', models.FloatField()),
                ('constructed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.Constructed')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.Part')),
            ],
        ),
    ]
