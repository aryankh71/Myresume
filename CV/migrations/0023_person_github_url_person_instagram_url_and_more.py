# Generated by Django 5.1 on 2024-10-14 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0022_remove_professionalsummary_summary_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='github_url',
            field=models.URLField(blank=True, null=True, verbose_name='لینک گیت هاب'),
        ),
        migrations.AddField(
            model_name='person',
            name='instagram_url',
            field=models.URLField(blank=True, null=True, verbose_name='لینک اینستاگرام'),
        ),
        migrations.AddField(
            model_name='person',
            name='skype_url',
            field=models.URLField(blank=True, null=True, verbose_name='لینک اسکایپ'),
        ),
        migrations.AlterField(
            model_name='person',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True, verbose_name='لینک تلگرام'),
        ),
    ]
