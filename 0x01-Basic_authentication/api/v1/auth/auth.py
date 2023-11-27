#!/usr/bin/env python3
"""Class to manage APIs"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class auth that will be used for flask request objects"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        will check whether authentication is required for a path. It
        will return True if path is None or excluded_paths is None/empty.
        Returns False if path is in excluded_paths.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] is not '/':
            path += '/'

        for paths in excluded_paths:
            if paths.endswith('*'):
                if path.startswith(paths[:-1]):
                    return False
            elif path == paths:
                return False
        
        return True

    def authorization_header(self, request=None) -> str:
        """
        Placeholder that retrieves authorization header and returns 
        None
        """
        if request is None:
            return None
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder method for getting the current user
        and returns none
        """
        return None
