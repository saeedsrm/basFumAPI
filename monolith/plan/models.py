from django.db import models
from accounts.models import Account


class Category(models.Model):
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی"

    name = models.CharField(max_length=100, verbose_name='Name')


class Plan(models.Model):
    class Meta:
        verbose_name = "برنامه ها"
        verbose_name_plural = "برنامه ها"

    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    cost = models.IntegerField(verbose_name='Cost')
    date = models.DateTimeField(verbose_name='date')
    duration = models.DateTimeField(verbose_name='Duratios')
    # organizor=models.ForeignKey()
    createor = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_finish = models.BooleanField(default=False)


class Plan_Category(models.Model):
    class Meta:
        verbose_name = "دسته بندی برنامه ها"
        verbose_name_plural = "دسته بندی برنامه ها"

    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class User_Plan(models.Model):
    class Meta:
        verbose_name = "لیست ثبت نامی در برنامه"
        verbose_name_plural = "لیست ثبت نامی در برنامه"

    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)


class Hashtak(models.Model):
    class Meta:
        verbose_name = "هشتک ها"
        verbose_name_plural = "هشتک ها"

    name = models.CharField(max_length=100, verbose_name='name')


class Plan_Hashtak(models.Model):
    class Meta:
        verbose_name = "ثبت هشتک برای برنامه ها"
        verbose_name_plural = "ثبت هشتک برای برنامه ها"

    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    hashtak = models.ForeignKey(Hashtak, on_delete=models.CASCADE)
