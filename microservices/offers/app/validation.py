# -*- coding: utf-8 -*-

from uuid import UUID

from config import Config


def is_valid_uuid(uuid_string):
    try:
        val = UUID(uuid_string, version=4)
    except ValueError:
        # If it's a value error, then the string
        # is not a valid hex code for a UUID.
        return False

    return str(val) == uuid_string


def is_valid_title(title):
    return len(title) <= Config.MAX_TITLE_LEN


def is_valid_text(title):
    return len(title) <= Config.MAX_TEXT_LEN
