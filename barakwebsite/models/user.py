from mongoengine import Document, fields
from .enums import UserRole, Block

class User(Document):
    username = fields.StringField(required=True, unique=True)
    email = fields.EmailField(required=True, unique=True)
    password_hash = fields.StringField(required=True)   # ⚠️ store hashed password, not plaintext

    hostel = fields.StringField(required=True, default="Barak")         # e.g. "Barak"
    block = fields.StringField(choices=Block.choices(), required=True)
    room_number = fields.IntField(required=True)
    phone_number = fields.StringField(required=True)

    role = fields.StringField(
        required=True,
        choices=UserRole.choices(),
        default=UserRole.STUDENT.value
    )

    meta = {"collection": "users"}

    def __str__(self):
        return f"{self.username} ({self.role})"