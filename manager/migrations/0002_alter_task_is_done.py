# Generated by Django 5.1.7 on 2025-03-31 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
