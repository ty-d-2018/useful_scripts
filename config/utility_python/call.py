import subprocess
from block.py import Blocks
from active.py import Activity

class VolunteerActivity:
    def __init__(self, name):
        super.__init__(name)


class Volunteer:
    def __init__(self):
        self.layers = []

    def add_block_layer(self, blocks, activity):
        self.layers.append((activity, blocks))

    def set_layer(self, blocks, activity, i):
        self.layers[i] = (activity, blocks)

    def get_layer(self, i):
        return self.layers[i]

    def run_layer(self, i):
        finish = self.get_layer_finish(i)
        return subprocess.run(finish, capture_output=True, text=True, check=True)

    # Activity needs to return a list
    def get_layer_finish(self, i):
        activity, blocks = self.layers[i]
        finish = blocks.loop_blocks(activity.read_block)

        return finish

    # Run activity on the results from the subprocess thread
    def run_and_process(self, i, activity):
        result = self.run_layer(i)
        pairs = {
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
        result_bl = Blocks(pairs)
        handle = process_blocks.loop_blocks(activity)

        return handle

    # Running run_and_process() for ever layer
    def process_all_layers(self, activity):
        handles = []
        for i in range(0, len(self.layers)):
            process = run_and_process(i, activity)
            handles.append(process)

        return handles