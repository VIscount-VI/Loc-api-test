# Generated by Django 4.2.4 on 2023-08-08 21:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]