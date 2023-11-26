#!/usr/bin/python3
"""Class to manage APIs"""
from flask import request



class Auth:
    """Class auth that will be used for flask request objects"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        will check whether authentication is required for a path. It
        will return True if path is None or excluded_paths is None/empty.
        Returns False if path is in excluded_paths.
        """
