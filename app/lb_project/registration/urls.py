from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('register/done/', views.done, name = 'register'),
    # Password reset URLs
    path("password-reset/", views.password_reset_view, name="password_reset"),
    path("password-reset/done/", views.password_reset_done, name="password_reset_done"),

]