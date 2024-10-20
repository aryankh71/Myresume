# Generated by Django 5.1 on 2024-10-12 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='field_of_study',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='education',
            name='institution',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
