# Generated by Django 2.2 on 2019-04-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolg_rl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='uv',
            field=models.PositiveIntegerField(default=1),
        ),
    ]