# Generated by Django 4.2.16 on 2024-10-01 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articles_timestamp_articles_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='updated',
            new_name='updated_at',
        ),
    ]
