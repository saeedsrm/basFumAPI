from django.db import models


class Courses(models.Model):
    class Meta:
        verbose_name = "درس ها"
        verbose_name_plural = "درس ها"

    name = models.CharField(max_length=60, verbose_name='نام دوره')
    description = models.TextField(verbose_name='توضیحات')
    cost = models.IntegerField(verbose_name="قیمت", default=0)
    isfinish = models.BooleanField(default=False, verbose_name="آیا دوره تمام شده است؟")
    language = models.CharField(default="فارسی", max_length=100, verbose_name="زبان")
    duration = models.IntegerField(null=True, verbose_name="مدت زمان دوره")
    level = models.CharField(null=True, max_length=100, verbose_name="سطح")
    number_of_seasons = models.IntegerField(default=1, verbose_name="تعداد فصل ها")
    teacher = models.CharField(null=True, max_length=60, verbose_name='مدرس')


class Chapter(models.Model):
    class Meta:
        verbose_name = "فصل ها"
        verbose_name_plural = "فصل ها"

    name = models.CharField(max_length=60, verbose_name='نام فصل')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name="درس")
    description = models.TextField(verbose_name='توضیحات')


class Movie(models.Model):
    class Meta:
        verbose_name = "فیلم ها"
        verbose_name_plural = "فیلم ها"

    movie = models.FileField(verbose_name='movie', upload_to='course_movie/')
    note = models.TextField(verbose_name='توضیحات')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name="فصل")


class Exam(models.Model):
    class Meta:
        verbose_name = "امتحانات"
        verbose_name_plural = "امتحانات"

    name = models.CharField(max_length=100, verbose_name='name')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)


class Question(models.Model):
    class Meta:
        verbose_name = "سوالات"
        verbose_name_plural = "سوالات"

    answer = models.CharField(verbose_name='answer', max_length=100)
    wrong_answer = models.CharField(verbose_name='wrong', max_length=100)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)


class User_Course(models.Model):
    class Meta:
        verbose_name = "لیست کاربران ثبت نامی در دوره"
        verbose_name_plural = "لیست کاربران ثبت نامی در دوره"

    user = models.IntegerField(verbose_name="کاربر")
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name="دوره")
