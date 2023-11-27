#!/usr/bin/env python3
"""The BasicAuth class"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """Implement Basic Authorization protocol methods"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Use the base 64 part of authorization for the
        basic authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[-1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode and return the value of the base64 as utf string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_value = base64.b64decode(base64_authorization_header)
            return decoded_value.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extract and return the user email and password from
        a decoded Base64 authorization header and returns
        a tuple with the email and password
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        email, password = decoded_base64_authorization_header.split(':', 1)
        return (email, password)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Return the Userinstance based on email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        except Exception:
            return None

        def current_user(self, request=None) -> TypeVar('User'):
            """Retrieve theUser instance for a request
            on basic Authentication
            """
            if request is None:
                return None

            authorization_header = request.headers.get('Authorization')

            base64_header = self.extract_base64_authorization_header(
                    authorization_header)

            decoded_credentials = self.decode_base64_authorization_header(
                    base64_header)

            user_email, user_pwd = self.extract_user_credentials(
                    decoded_credentials)

            user_instance = self.user_object_from_credentials(
                    user_email, user_pwd)

            return user_instance
