from django.urls import path
from accounts.views import MyObtainTokenPairView, PostCreateAPIView, GetMyInformation
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf.urls import url

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^create', PostCreateAPIView.as_view(), name='create'),
    url(r'^myinfo', GetMyInformation.as_view(), name='get-informations'),
]
