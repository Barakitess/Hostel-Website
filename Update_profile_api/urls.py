from django.urls import path
from .views import PublicProfileUpdateView

urlpatterns = [
    path('update-profile/<int:id>/',
         PublicProfileUpdateView.as_view(), name='update-profile'),
]
