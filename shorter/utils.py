import os
import pyqrcode
from short.settings import MEDIA_ROOT


def qr_code_gen(code, url):
    qr = pyqrcode.create(f'{url}')
    folder = MEDIA_ROOT + '/qr_codes/'
    if not os.path.exists(folder):
        os.mkdir(folder)
    path = f'qr_codes/{code}.png'
    file_path = MEDIA_ROOT + '/' + path
    qr.png(f'{file_path}', scale=5)
    return path
