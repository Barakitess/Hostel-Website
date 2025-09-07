from enum import Enum


class UserRole(str, Enum):
    STUDENT = "student"
    MAINTAINER = "maintainer"
    ADMIN = "admin"

    @classmethod
    def choices(cls):
        return [role.value for role in cls]


class Block(str, Enum):
    A = "A"
    B = "B"

    @classmethod
    def choices(cls):
        return [block.value for block in cls]
