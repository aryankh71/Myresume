# Generated by Django 5.1 on 2024-10-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0013_alter_professionalsummary_career_goals_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='professionalsummary',
            name='summary_file',
            field=models.FileField(blank=True, null=True, upload_to='%Y-%m-%d', verbose_name='تصویر رزومه'),
        ),
    ]
