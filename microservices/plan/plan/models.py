from django.db import models
from monolith.accounts.models import Account


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')


class Plan(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    cost = models.IntegerField(verbose_name='Cost')
    date = models.DateTimeField(verbose_name='date')
    duration = models.DateTimeField(verbose_name='Duratios')
    # organizor=models.ForeignKey()
    createor = models.ForeignKey(Account, on_delete=models.CASCADE)


class Plan_Category(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class User_Plan(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)


class Hashtak(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')


class Plan_Hashtak(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    hashtak = models.ForeignKey(Hashtak, on_delete=models.CASCADE)
