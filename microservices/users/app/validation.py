# -*- coding: utf-8 -*-

import re
from uuid import UUID

from passlib.hash import sha256_crypt

from config import Config


def is_valid_username(username):
    if len(username) < Config.LOGIN_MIN_LENGTH:
        return False
    if len(username) > Config.LOGIN_MAX_LENGTH:
        return False
    if not is_valid_chars(username):
        return False
    return True


def is_valid_hash(password_hash):
    return sha256_crypt.identify(password_hash)


def is_valid_uuid(uuid_string):
    try:
        val = UUID(uuid_string, version=4)
    except ValueError:
        # If it's a value error, then the string
        # is not a valid hex code for a UUID.
        return False

    return val.hex == uuid_string


def is_valid_chars(word):
    res = re.search(r"[^\w\]\[?/<~#`!@$%^&*()+=}|:\";',>\-_]", word)
    return res is None
