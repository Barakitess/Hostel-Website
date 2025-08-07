from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class ProfileUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.first_name')
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = Profile
        fields = ['name', 'email', 'roll_no', 'room_no', 'mobile']

    def update(self, instance, validated_data):
        # Handle user fields
        user_data = validated_data.pop('user', {})
        if 'first_name' in user_data:
            instance.user.first_name = user_data['first_name']
        if 'email' in user_data:
            instance.user.email = user_data['email']
        instance.user.save()

        # Handle profile fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
