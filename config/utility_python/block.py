from argument import Argument

class Blocks:
    def __init__(self, pairs={}):
        self.pairs = {}
        self.k = None
        self.i = 0
        self.name = "block"

        self.set_pairs_keys(pairs)

    def set_pair_keys(self, pair):
        self.pair = pair
        self.k = self.get_keys()

    def get_keys(self):
        return self.pair.keys()

    def get_block(self):
        if self.is_empty():
            return None
        name = self.k[self.i]
        block = self.get_value(name)
        self.increase_count()

        return(name, block)

    def increase_count(self):
        if self.i >= len(self.k):
            self.i = 0
        else:
            self.i = self.i + 1

    def loop_blocks(self, activity):
        name, block = self.get_block()
        while self.i > 0:
            activity(name, block)
            name, block = self.get_block()

    def get_value(self, key):
        return self.pairs[key]

    def is_empty(self):
        if len(self.k) == 0:
            return True
        return False

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

