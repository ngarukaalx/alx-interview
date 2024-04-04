#!/usr/bin/python3
"""unicode transformation format"""


def validUTF8(data):
    """determines if a given data
    set represents a valid UTF-8 encoding
    """
    follow = 0
    for i in data:
        bi = bin(i & 0xFF)[2:].zfill(8)
        if follow == 0:
            if bi.startswith('0'):
                continue
            elif bi.startswith('110'):
                follow = 1
            elif bi.startswith('1110'):
                follow = 2
            elif bi.startswith('11110'):
                follow = 3
            else:
                return False
        else:
            if not bi.startswith('10'):
                return False
            follow -= 1
    return follow == 0
