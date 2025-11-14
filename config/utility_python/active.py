
class Activity:
    def __init__(self, name):
        self.name = name
        
    def get_label(self):
        return self.name

    def read_block(self, name, block):
        return f"I have the block named: {name}"

    def read_set_block(self, allBlocks):
        pass

    def read_sequence(self, sequence):
        pass