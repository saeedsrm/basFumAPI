from django.db import models
from accounts.models import Account
from plan.models import Plan
from courses.models import Courses


class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="کاربر")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, verbose_name="برنامه", null=True, blank=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name="دوره", null=True, blank=True)
    date = models.DateTimeField(auto_now=True, verbose_name='زمان')
    comment = models.TextField(verbose_name="نظر")
