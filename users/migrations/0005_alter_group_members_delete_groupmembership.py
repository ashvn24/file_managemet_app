# Generated by Django 5.0.4 on 2024-04-13 07:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_groupmembership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='group_members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='GroupMembership',
        ),
    ]