from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=60, verbose_name='name')
    description = models.TextField(verbose_name='Description')


class Movie(models.Model):
    movie = models.FileField(verbose_name='movie', upload_to='course_movie/')
    note = models.TextField(verbose_name='Note')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)


class Exam(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)


class Question(models.Model):
    answer = models.CharField(verbose_name='answer' ,max_length=100)
    wrong_answer = models.CharField(verbose_name='wrong',max_length=100)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
