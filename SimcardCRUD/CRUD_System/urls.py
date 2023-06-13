from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.main, name="main-page"),
    path("login/", views.login_request, name="login-request"),
    path('logout/', views.logout_request, name="logout-request"),
]