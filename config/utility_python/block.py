from argument import Argument

class Blocks(Argument):
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