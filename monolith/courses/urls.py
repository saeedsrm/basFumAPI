from django.conf.urls import url
from courses import views

app_name='courses'

urlpatterns = [
    url(r'^$', views.CoursesPostListAPIView.as_view(), name='post-list'),
    url(r'^(?P<id>\d+)$', views.CoursesPostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<id>\d+)/edit', views.CoursesPostUpdateAPIView.as_view(), name='update'),
    url(r'^create', views.CoursesPostCreateAPIView.as_view(), name='create'),
    url(r'^(?P<id>\d+)/delete', views.CoursesPostDeleteAPIView.as_view(), name='delete'),
    url(r'^register-in-course', views.UserCourseCreateAPIView.as_view(), name='UserCourseCreateAPIView'),
    url(r'^list-of-my-course', views.UserCoursesListAPIView.as_view(), name='UserCoursesListAPIView'),
]