from argument.py import Argument
from block.py import Blocks

class BlocksArgument(Blocks):
    def __init__(self, tags):
        self.arguments = Argument(tags)
        Blocks.__init__(self.arguments.get_parsed())