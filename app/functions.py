import secrets
import os.path
import os
from flask import current_app
from PIL import Image

def save_pictures(pictures):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(pictures.filename)
    picture_fn = random_hex + f_ext
    pictures_path = os.path.join(current_app.config['SERVER_PATH'], picture_fn)
    pictures_path = os.path.join(current_app.config['SERVER_PATH'], picture_fn)

    output_size = (125, 125)
    i = Image.open(pictures)
    i.thumbnail(output_size)
    i.save(pictures_path)
    return picture_fn
    