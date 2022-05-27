from django.contrib import admin
from courses import models


@admin.register(models.Courses)
class CoursesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Exam)
class ExamAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

