# backend/server/apps/accounts file
from django.urls import path, include
# from django.urls import include, re_path

urlpatterns = [
    path(r'^api/v1/', include('djoser.urls')),
    path(r'^api/v1/', include('djoser.urls.authtoken')),
]