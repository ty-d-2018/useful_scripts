from config.utility_python.argument import Argument

class Blocks:
    def __init__(self, pairs={}):
        self.pairs = {}
        self.road = None
        self.i = 0
        self.name = "block"

        self.set_pair_keys(pairs)

    def set_pair_keys(self, pair):
        self.pairs = pair
        self.road = list(self.get_keys())

    def get_keys(self):
        return self.pairs.keys()

    def get_block(self):
        if self.is_empty():
            return None
        print(f"i is at {self.i}")
        name = self.get_sequence()[self.i]
        block = self.get_value(name)
        self.increase_count()

        return(name, block)

    def get_sequence(self):
        return self.road

    def increase_count(self):
        if self.i >= (self.get_key_size() - 1):
            self.i = 0
        else:
            self.i = self.i + 1

    def loop_blocks(self, activity):
        for indexElement in range(0, self.get_key_size()):
            name, block = self.get_block()
            activity(name, block)

    def loop_set(self, activity):
        activity(self)

    def loop_order(self, activity):
        activity(self.road)

    def get_value(self, key):
        return self.pairs[key]

    def is_empty(self):
        if len(self.get_sequence()) == 0:
            return True
        return False

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_key_size(self):
        return len(self.get_sequence())

