from argument import Argument

class Block:
    def __init__(self, pairs):
        self.pairs = {}
        self.k = None
        self.i = 0

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

class BlockArgument(Argument):
    def __init__(self, tags):
        super().__init__(tags)
        self.pArgs = self.get_parsed()
        self.k = var(self.pArgs).keys()
        self.i = 0

    def get_option(self, name):
        optionValue = getattr(self.argParse, name)
        return optionValue

    def get_block(self):
        if self.is_empty():
            return None
        name = self.k[self.i]
        block = get_option(name)
        self.increase_count()

        return (name, block)

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

    def is_empty(self):
        if len(self.k) == 0:
            return True
        return False