from texture import Texture

class Scene:
    def __init__(self):
        from loader import assets

        self.assets = assets
        self.tiles = {}
        
        print(assets)
        
    def add_tile(self, x: int, y: int, sheet: Texture, name: str) -> None:
        pass
