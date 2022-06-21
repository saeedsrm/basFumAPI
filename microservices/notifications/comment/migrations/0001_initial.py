# Generated by Django 3.2.6 on 2022-06-21 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(verbose_name='کاربر')),
                ('plan', models.IntegerField(blank=True, null=True, verbose_name='برنامه')),
                ('course', models.IntegerField(blank=True, null=True, verbose_name='دوره')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='زمان')),
                ('comment', models.TextField(verbose_name='نظر')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظر',
            },
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('note', models.TextField(verbose_name='اطلاعیه')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='زمان')),
            ],
            options={
                'verbose_name': 'اطلاعیه ها',
                'verbose_name_plural': 'اطلاعیه ها',
            },
        ),
    ]