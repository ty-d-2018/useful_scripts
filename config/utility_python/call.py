import subprocess
from block.py import Blocks
from active.py import Activity

class Volunteer:
    def __init__(self):
        self.layers = []

    def add_block_layer(self, blocks, activity):
        self.layers.append((activity, blocks))

    def run_layer(self, i):
        finish = self.get_layer_finish(i)
        return subprocess.run(finish, capture_output=True, text=True, check=True)

    def get_layer_finish(self, i):
        activity, blocks = self.layers[i]
        finish = blocks.loop_blocks(activity.read_block)

        return finish

class CallingCommand:
    def __init__(self, commandMap):
        self.commands = []
        for key, value in commandMap.items():
            tempC = []
            tempC.append(key)
            tempC.append(value)
            self.commands.append(tempC)
        
    def execute_command(self, c):
        return subprocess.run(c, capture_output=True, text=True, check=True)

    def run_all_commands(self):
        results = []
        for command in self.commands:
            results.append(self.execute_command(command))
        
        return results

    def run_a_command(self, i):
        result = self.execute_command(self.commands[i])

        return result

    def get_commands(self):
        return self.commands