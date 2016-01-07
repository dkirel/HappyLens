import os
import re

from .models import Photo

def generate_photo(file_path):
    photo_path, width, height = image_utils.fit_and_save(file_path)
    thumb_path = image_utils.generate_thumbnail(photo_path)
    photo_path, thumb_path = (relp(rp(p), PARENT_DIR) for p in (photo_path, thumb_path))
    photo = Photo(image_path=photo_path, thumbnail_path=thumb_path, width=width, height=height)
    photo.save()
    return photo


def save_file(file, file_path):
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
