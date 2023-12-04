#!/usr/bin/env python3
"""
The main file
"""
from user import User

print(User.__tablename__)

for column in User.__table.__columns:
    print("{}: {}".format(column, column.type))
