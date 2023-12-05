#!/usr/bin/env python3
"""Define sthe hash_password method
takes in a pasword string argument and
returns bytes
"""
import bcrypt
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound
from typing import (
    TypeVar,
    Union
)

from db import DB
from user import User

U = TypeVar(User)


def _hash_password(password: str) -> bytes:
    """The hashed password string that returns the hash
    in bytes"""
    passwd = password.encode('utf-8')
    return bcrypt.hashpw(passwd, bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a uuid and return its string type
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database
    """

    def __init__(self):
        self._db = DB()

def register_user(self, email: str, password: str) -> User:
    """The Auth function that takes email and password
    Args:
        email (str): the user's email
        password (str): the user's password
    Return:
        creates new user if no user with a given email exists
        or else raises the ValueError
    """
    try:
        user = self._db.find_user_by(email=email)
    except NoResultFound:
        hashed = _hash_password(password)
        usr = self._db.add_user(email, hashed)
        return usr
    raise ValueError(f"User {email} already exists")
