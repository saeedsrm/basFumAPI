from django.contrib import admin
from comment.models import Comment, Notifications


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'date', 'comment',)


@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'note', 'date',)
