# Generated by Django 5.1 on 2024-10-13 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0018_costomuser'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CostomUser',
            new_name='CustomUser',
        ),
    ]
