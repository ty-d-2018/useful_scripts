from argument import Argument

class Blocks(Argument):
    def __init__(self, tags):
        super().__init__(tags)
        self.k = var(self.param_keys).keys()
        self.i = 0

    def get_block(self):
        if self.is_empty():
            return None
        block = self.get_option(self.k[self.i])
        self.increase_count()

        return block

    def increase_count(self):
        if self.i >= len(self.k):
            self.i = 0
        else:
            self.i = self.i + 1

    def loop_blocks(self, action):
        block = self.get_block()
        while self.i > 0:
            action(block)
            block = self.get_block()

    def is_empty(self):
        if len(self.k) == 0:
            return True
        return False