from django.db import models


class Comment(models.Model):
    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظر"

    user = models.IntegerField(verbose_name="کاربر")
    plan = models.IntegerField(verbose_name="برنامه", null=True, blank=True)
    course = models.IntegerField(verbose_name="دوره", null=True, blank=True)
    date = models.DateTimeField(auto_now=True, verbose_name='زمان')
    comment = models.TextField(verbose_name="نظر")


class Notifications(models.Model):
    class Meta:
        verbose_name = "اطلاعیه ها"
        verbose_name_plural = "اطلاعیه ها"

    title = models.CharField(max_length=100, verbose_name="عنوان")
    note = models.TextField(verbose_name="اطلاعیه")
    date = models.DateTimeField(auto_now=True, verbose_name='زمان')
