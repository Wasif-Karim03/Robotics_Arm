class Block:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color
        self.on_top_of = None  # Current support block or None for ground

    def __repr__(self):
        return f"{self.name}(Size: {self.size}, Color: {self.color})"

class BlocksWorld:
    def __init__(self):
        self.blocks = {}
        self.ground = []

    def add_block(self, name, size, color):
        block = Block(name, size, color)
        self.blocks[name] = block
        self.ground.append(block)

    def display_world(self):
        for block in self.blocks.values():
            on = block.on_top_of.name if block.on_top_of else "ground"
            print(f"{block.name} is on {on}")
