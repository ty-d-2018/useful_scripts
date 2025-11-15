import subprocess
from config.utility_python.block import Blocks
from config.utility_python.active import Activity

class VolunteerActivity(Activity):
    def __init__(self, name):
        super().__init__(name)
        self.options = []

    def get_list(self):
        return self.options

    def clear(self):
        self.options = []


class Volunteer:
    def __init__(self):
        self.layers = {}

    def add_layer(self, command_activity):
        self.layers.append(command_activity.give_command())

    def set_layer(self, command_activity):
        self.layers[i] = command_activity.give_command()

    def get_layer(self, i):
        return self.layers[i]

    def run_layer(self, i):
        return subprocess.run(self.get_layer(i), capture_output=True, text=True, check=True)

    def run_all_layers(self):
        results = []
        for i in range(0, len(self.layers)):
            results.append(self.run_layer(i))

        return results

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