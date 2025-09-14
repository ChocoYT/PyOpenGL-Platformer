import json, os
from PIL       import Image
from OpenGL.GL import *

from texture_array import TextureArray

def load_directory(root: str) -> dict:
    image_paths = []

    meta = {}

    for current_dir, _, files in os.walk(root):
        for file in files:
            full_path = os.path.join(current_dir, file)
            ext       = os.path.splitext(file)[1].lower()

            # Collect Images
            if ext == ".png" and can_load(full_path):
                image_paths.append(full_path)

            # Collect JSON Metadata
            elif ext == ".json":
                with open(full_path, "r") as f:
                    data = json.load(f)

                    # Tiles
                    if "tiles" in data:
                        if meta.get("tiles") is None:
                            meta["tiles"] = {}
                            
                        for name, coords in data["tiles"].items():
                            meta["tiles"][name] = coords
                    
                    # Tile Size
                    if "tile_size" in data:
                        if meta.get("tile_size") is None:
                            meta["tile_size"] = data["tile_size"]
                        elif meta["tile_size"] != data["tile_size"]:
                            print(f"Warning: Tile size mismatch in {file}")

    textures = TextureArray(image_paths)

    return {
        "textures": textures,
        "meta": meta
    }

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
