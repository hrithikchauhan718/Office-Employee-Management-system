# Generated by Django 5.0 on 2024-04-02 18:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
