# Generated by Django 5.0 on 2024-01-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0002_task_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="date",
            field=models.DateField(default="2024-08-01"),
            preserve_default=False,
        ),
    ]
