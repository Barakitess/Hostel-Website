from barakwebsite.models.user import User

class UserRepository:
    @staticmethod
    def create_user(username, email, password_hash, hostel, block, room_number, phone_number, role):
        user = User(
            username=username,
            email=email,
            password_hash=password_hash,
            hostel=hostel,
            block=block,
            room_number=room_number,
            phone_number=phone_number,
            role=role,
        )
        user.save()
        return user

    @staticmethod
    def get_by_username(username):
        return User.objects(username=username).first()

    @staticmethod
    def get_by_email(email):
        return User.objects(email=email).first()
