from django.conf.urls import url
from comment import views

app_name = 'comment'

urlpatterns = [
    url(r'^create-comment', views.CommentCreateAPIView.as_view(), name='create-comment'),
    url(r'^list-of-comment', views.CommentListAPIView.as_view(), name='CommentListAPIView'),
]
