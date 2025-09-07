from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from barakwebsite.services.user_service import UserService

class UserCreateView(APIView):
    def post(self, request):
        data = request.data
        try:
            user = UserService.create_user(
                username=data.get("username"),
                email=data.get("email"),
                password=data.get("password"),  # raw password (will be hashed)
                hostel=data.get("hostel", "Barak"),
                block=data.get("block"),
                room_number=data.get("room_number"),
                phone_number=data.get("phone_number"),
                role=data.get("role", "student"),
            )
            return Response(
                {
                    "message": "User created successfully",
                    "user": {
                        "id": str(user.id),
                        "username": user.username,
                        "email": user.email,
                        "role": user.role,
                        "hostel": user.hostel,
                        "block": user.block,
                        "room_number": user.room_number,
                        "phone_number": user.phone_number,
                    },
                },
                status=status.HTTP_201_CREATED,
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)

        user = UserService.login(username, password)
        if not user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            "message": "Login successful",
            "username": user.username,
            "role": user.role
        }, status=status.HTTP_200_OK)