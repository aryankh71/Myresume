# Generated by Django 5.1 on 2024-10-13 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0021_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professionalsummary',
            name='summary_file',
        ),
    ]
