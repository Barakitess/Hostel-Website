from django.urls import path
from .views.user_view import UserCreateView, LoginView, UpdateUserView

urlpatterns = [
    path("api/users/create/", UserCreateView.as_view(), name="create-user"),
    path("api/users/login/", LoginView.as_view(), name="login"),
    path("api/users/<str:username>/update/", UpdateUserView.as_view(), name="update_user"),
]
