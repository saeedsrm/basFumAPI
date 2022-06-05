from django.conf.urls import url
from plan import views

app_name = 'plan'

urlpatterns = [
    url(r'^$', views.PlanPostListAPIView.as_view(), name='post-list'),
    url(r'^(?P<id>\d+)$', views.PlanPostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<id>\d+)/edit', views.PlanPostUpdateAPIView.as_view(), name='update'),
    url(r'^create', views.PlanPostCreateAPIView.as_view(), name='create'),
    url(r'^(?P<id>\d+)/delete', views.PlanPostDeleteAPIView.as_view(), name='delete'),
    url(r'^register-in-plan', views.UserPlanCreateAPIView.as_view(), name='UserPlanCreateAPIView'),
    url(r'^list-my-plan', views.ListMyPlanAPIView.as_view(), name='ListMyPlanAPIView'),

]
