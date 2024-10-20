# Generated by Django 5.1 on 2024-10-14 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0023_person_github_url_person_instagram_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='telegram_url',
            field=models.URLField(blank=True, null=True, verbose_name='لینک تلگرام'),
        ),
        migrations.AlterField(
            model_name='person',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True, verbose_name='لینک لینکدین'),
        ),
    ]
