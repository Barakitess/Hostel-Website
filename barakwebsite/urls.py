from django.urls import path
from .views.user_view import UserCreateView

urlpatterns = [
    path("api/users/create/", UserCreateView.as_view(), name="create-user"),
]
