# Generated by Django 3.1.3 on 2021-10-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
