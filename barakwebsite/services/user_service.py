from barakwebsite.repositories.user_repository import UserRepository
from barakwebsite.models.enums import UserRole, Block
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    @staticmethod
    def create_user(username, email, password, hostel, block, room_number, phone_number, role=UserRole.STUDENT.value):
        # Validate role
        if role not in UserRole.choices():
            raise ValueError(f"Invalid role: {role}")

        # Validate block
        if block not in Block.choices():
            raise ValueError(f"Invalid block: {block}")

        # Check uniqueness
        if UserRepository.get_by_username(username):
            raise ValueError(f"Username '{username}' already exists")
        if UserRepository.get_by_email(email):
            raise ValueError(f"Email '{email}' already exists")

        # Hash password
        password_hash = generate_password_hash(password)

        # Save to repository
        return UserRepository.create_user(
            username=username,
            email=email,
            password_hash=password_hash,
            hostel=hostel,
            block=block,
            room_number=room_number,
            phone_number=phone_number,
            role=role,
        )

    @staticmethod
    def login(username, password):
        user = UserRepository.get_by_username(username)
        if not user:
            raise ValueError("Invalid username or password")

        if not check_password_hash(user.password_hash, password):
            raise ValueError("Invalid username or password")

        return user

    @staticmethod
    def update_user(username, update_data: dict):
        # Validate block if provided
        if "block" in update_data and update_data["block"] not in Block.choices():
            raise ValueError(f"Invalid block: {update_data['block']}")

        # Validate role if provided
        if "role" in update_data and update_data["role"] not in UserRole.choices():
            raise ValueError(f"Invalid role: {update_data['role']}")

        updated_user = UserRepository.update_user(username, update_data)
        if not updated_user:
            raise ValueError("User not found")

        return updated_user

