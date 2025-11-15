import subprocess
from config.utility_python.block import Blocks
from config.utility_python.active import Activity

class VolunteerActivity(Activity):
    def __init__(self, name):
        super().__init__(name)
        self.current_command = []
        self.results = []

    def new_command(self, command_list):
        self.current_command = command_list

    def add_to_volunteer_blocks(self, volunteer_blocks):
        if len(self.current_command) == 0:
            return

        keys = volunteer_blocks.get_key_list()
        current_layer_count = len(keys) - 1
        new_count = current_layer_count + 1
        volunteer_blocks.add_pair(new_count, self.current_command)
        
        self.clear_commands()

    def run_block(self, name, block):
        result = subprocess.run(block, capture_output=True, text=True, check=True)
        self.results.append(result)

    def get_list(self):
        return self.options

    def clear(self):
        self.results = []

    def clear_commands(self):
        self.current_command = []

    def get_results(self):
        final_results = self.results
        self.clear()

        return final_results

class Volunteer(Blocks):
    def __init__(self):
        super().__init__()
