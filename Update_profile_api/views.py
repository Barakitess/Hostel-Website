from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Profile
from .serializers import ProfileUpdateSerializer


class PublicProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    lookup_field = 'id'  # So you can use /update-profile/<id>/
