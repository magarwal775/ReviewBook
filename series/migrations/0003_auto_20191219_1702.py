# Generated by Django 3.0 on 2019-12-19 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0002_auto_20191215_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='avg_review',
            new_name='avgrating',
        ),
        migrations.RenameField(
            model_name='episode',
            old_name='nor',
            new_name='totalrating',
        ),
        migrations.RenameField(
            model_name='episode',
            old_name='total_review',
            new_name='totalreview',
        ),
    ]