from django.conf.urls import url
from plan import views

app_name='plan'

urlpatterns = [
    url(r'^$', views.PostListAPIView.as_view(),name='post-list'),
    url(r'^(?P<id>\d+)$', views.PostDetailAPIView.as_view(),name='detail'),
    url(r'^(?P<id>\d+)/edit', views.PostUpdateAPIView.as_view(),name='update'),
    url(r'^create', views.PostCreateAPIView.as_view(),name='create'),
    url(r'^(?P<id>\d+)/delete', views.PostDeleteAPIView.as_view(),name='delete'),
]