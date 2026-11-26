"""Hello, Pyxel: 色が変わる文字と、横へ動く四角。Escで終わる。"""

import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, title="Hello, Pyxel")
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.rect(self.x, 60, 8, 8, 9)


App()
