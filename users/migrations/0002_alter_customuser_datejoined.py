# Generated by Django 5.0.4 on 2024-04-13 05:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='dateJoined',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]