# -*- coding: utf-8 -*-

import re

LOGIN_MAX_LENGTH = 32
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 32
UUID_LENGTH = 36


def is_valid_username(username):
    if len(username) > LOGIN_MAX_LENGTH:
        return False
    if not is_valid_chars(username):
        return False
    return True


def is_valid_password(password):
    if len(password) < PASSWORD_MIN_LENGTH or len(password) > PASSWORD_MAX_LENGTH:
        return False
    if not is_valid_chars(password):
        return False
    return True


def is_valid_uuid(uuid):
    if not len(uuid) == UUID_LENGTH:
        return False
    res = re.search(r"[^\w-]", uuid)
    return res is None


def is_valid_chars(word):
    res = re.search(r"[^\w\]\[?/<~#`!@$%^&*()+=}|:\";',>\-_]", word)
    return res is None
