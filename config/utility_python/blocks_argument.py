from argument.py import Argument
from block.py import Blocks

class BlocksArgument(Blocks):
    def __init__(self, tags, argument):
        self.arguments = argument
        self.arguments.set_tags(tags)
        Blocks.__init__(self.arguments.get_parsed())