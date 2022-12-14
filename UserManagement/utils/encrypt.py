import hashlib
from excriseProject import settings


def md5(data_string):
    object = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    object.update(data_string.encode('utf-8'))
    return object.hexdigest()
