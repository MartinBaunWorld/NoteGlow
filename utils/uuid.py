from shortuuid import uuid as _uuid


def uuid():
    return str(_uuid())
