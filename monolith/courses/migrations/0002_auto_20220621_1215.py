# Generated by Django 3.2.13 on 2022-06-21 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'verbose_name': 'فصل ها', 'verbose_name_plural': 'فصل ها'},
        ),
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name': 'درس ها', 'verbose_name_plural': 'درس ها'},
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': 'امتحانات', 'verbose_name_plural': 'امتحانات'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'فیلم ها', 'verbose_name_plural': 'فیلم ها'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'سوالات', 'verbose_name_plural': 'سوالات'},
        ),
        migrations.AlterModelOptions(
            name='user_course',
            options={'verbose_name': 'لیست کاربران ثبت نامی در دوره', 'verbose_name_plural': 'لیست کاربران ثبت نامی در دوره'},
        ),
    ]
