from PIL import Image
from OpenGL.GL import *
import os

from texture import Texture

def load_directory(directory: str) -> dict:
    assets = {}

    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        
        if os.path.isdir(full_path):
            assets[entry] = load_directory(full_path)
            continue
        elif os.path.isfile(full_path) and can_load(full_path):
            try:
                assets[entry] = Texture(full_path)
            except Exception as e:
                print(f"Failed to Load {full_path}: {e}")

    return assets

def can_load(path: str) -> bool:
    try:
        with Image.open(path) as img:
            img.verify()
        return True
    except Exception:
        return False

assets = {}

def load_assets() -> None:
    global assets
    assets = load_directory("Assets")
