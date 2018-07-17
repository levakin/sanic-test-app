# -*- coding: utf-8 -*-

import re

UUID_LENGTH = 36


def is_valid_uuid(uuid):
    if not len(uuid) == UUID_LENGTH:
        return False
    res = re.search(r"[^\w-]", uuid)
    return res is None
