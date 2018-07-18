# -*- coding: utf-8 -*-

import re
import settings

UUID_LENGTH = 36


def is_valid_uuid(uuid):
    if not len(uuid) == UUID_LENGTH:
        return False
    res = re.search(r"[^\w-]", uuid)
    return res is None


def is_valid_title(title):
    return len(title) <= settings.MAX_TITLE_LEN


def is_valid_text(title):
    return len(title) <= settings.MAX_TEXT_LEN
