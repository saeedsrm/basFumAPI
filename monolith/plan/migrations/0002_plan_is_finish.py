# Generated by Django 3.2.6 on 2022-06-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='is_finish',
            field=models.BooleanField(default=False),
        ),
    ]
