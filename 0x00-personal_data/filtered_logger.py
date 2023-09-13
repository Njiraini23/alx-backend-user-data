#!/usr/bin/env python3
"""A function called filter_datum that returns
long message obfscated"""
import logging
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
               separator: str) -> str:
    """A function that returns the log mesage obfuscated"""
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
        return message
