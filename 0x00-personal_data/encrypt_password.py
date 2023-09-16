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
