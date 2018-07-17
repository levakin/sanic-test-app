# -*- coding: utf-8 -*-

import re
from passlib.hash import sha256_crypt

LOGIN_MAX_LENGTH = 32
UUID_LENGTH = 36


def is_valid_username(username):
    if len(username) > LOGIN_MAX_LENGTH:
        return False
    if not is_valid_chars(username):
        return False
    return True


def is_valid_hash(password_hash):
    return sha256_crypt.identify(password_hash)


def is_valid_uuid(uuid):
    if not len(uuid) == UUID_LENGTH:
        return False
    res = re.search(r"[^\w-]", uuid)
    return res is None


def is_valid_chars(word):
    res = re.search(r"[^\w\]\[?/<~#`!@$%^&*()+=}|:\";',>\-_]", word)
    return res is None
