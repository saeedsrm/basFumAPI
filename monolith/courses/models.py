from django.db import models
from accounts.models import Account


class Courses(models.Model):
    name = models.CharField(max_length=60, verbose_name='نام دوره')
    description = models.TextField(verbose_name='توضیحات')
    cost = models.IntegerField(verbose_name="قیمت", default=0)
    isfinish = models.BooleanField(default=False, verbose_name="آیا دوره تمام شده است؟")
    language = models.CharField(default="فارسی", max_length=100, verbose_name="زبان")
    duration = models.IntegerField(null=True, verbose_name="مدت زمان دوره")
    level = models.CharField(null=True, max_length=100, verbose_name="سطح")
    number_of_seasons = models.IntegerField(default=1, verbose_name="تعداد فصل ها")
    teacher = models.CharField(null=True, max_length=60, verbose_name='مدرس')


class Movie(models.Model):
    movie = models.FileField(verbose_name='movie', upload_to='course_movie/')
    note = models.TextField(verbose_name='توضیحات')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name="درس")


class Exam(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)


class Question(models.Model):
    answer = models.CharField(verbose_name='answer', max_length=100)
    wrong_answer = models.CharField(verbose_name='wrong', max_length=100)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)


class User_Course(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="کاربر")
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name="دوره")
