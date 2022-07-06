# Generated by Django 4.0.5 on 2022-07-02 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journalAppD', '0002_rename_ressource_resource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='link',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='name',
        ),
        migrations.AddField(
            model_name='resource',
            name='content',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='resource',
            name='title',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
