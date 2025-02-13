# Generated by Django 3.1.3 on 2020-11-28 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180725_0926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_pub']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='post',
            name='users',
            field=models.TextField(default=django.utils.timezone.now, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
