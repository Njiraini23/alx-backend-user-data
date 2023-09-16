#!/usr/bin/env python3
""" Hash_password function that expects one string"""
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    "Using bcrypt to perfom hashing"
    encode = password.encode()
    salt = bcrypt.gensalt()
    hashed = hashpw(encode, salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Compare whether password is same as hashed password
    Args:
        hashed_password (bytes): hashed passwrd
        password (str): password in the string
    returns:
        a bool
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
