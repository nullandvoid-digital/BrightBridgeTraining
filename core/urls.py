from django.urls import path, include

from . import views

urlpatterns = [
    path("account/", views.user_profile, name="user_profile"),
    path("account/edit/", views.edit_profile, name="edit_profile"),
]
