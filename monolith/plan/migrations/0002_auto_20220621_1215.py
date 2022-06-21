# Generated by Django 3.2.13 on 2022-06-21 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی'},
        ),
        migrations.AlterModelOptions(
            name='hashtak',
            options={'verbose_name': 'هشتک ها', 'verbose_name_plural': 'هشتک ها'},
        ),
        migrations.AlterModelOptions(
            name='plan',
            options={'verbose_name': 'برنامه ها', 'verbose_name_plural': 'برنامه ها'},
        ),
        migrations.AlterModelOptions(
            name='plan_category',
            options={'verbose_name': 'دسته بندی برنامه ها', 'verbose_name_plural': 'دسته بندی برنامه ها'},
        ),
        migrations.AlterModelOptions(
            name='plan_hashtak',
            options={'verbose_name': 'ثبت هشتک برای برنامه ها', 'verbose_name_plural': 'ثبت هشتک برای برنامه ها'},
        ),
        migrations.AlterModelOptions(
            name='user_plan',
            options={'verbose_name': 'لیست ثبت نامی در برنامه', 'verbose_name_plural': 'لیست ثبت نامی در برنامه'},
        ),
    ]
