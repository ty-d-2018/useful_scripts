from config.utility_python.block import Blocks
from config.utility_python.active import Activity
from config.utility_python.template import Template, Value

def create_map():
    arg_map = {
        "#FILENAME": "file-path",
        "#NUMBER": "numerial",
        "#DIRECTORY": "directory-path",
        "#CHARACTERS": "text"
    }

    return arg_map

class AcitvateCommand(Activity):
    def __init__(self, values, command_call):
        super().__init__("template-activity")
        self.values = values
        self.options = []
        self.call = command_call

    def get_size(self):
        return len(self.values)

    def set_count(self, i):
        self.count = i

    def get_value(self, i):
        return self.values[i]

    def get_option(self, i):
        return self.options[i]

    def get_command_call(self):
        return self.call

    def read_block(self, name, block):
        argument = ""
        if len(name) == 1:
            argument = f"-{name}"
        else:
            argument = f"--{name}"
        self.options.append(name)

    def give_command(self):
        command_list = []
        command_list.append(self.get_command_call())
        for i in range(0, self.get_size()):
            command_list.append(self.get_option(i))
            command_list.append(self.get_value(i))

        return command_list
            

class CommandBlock(Blocks):
    def __init__(self, name):
        super().__init__()
        self.set_name(name)

    def to_pairs(self, json_object):
        options = json_object["options"]
        command_pairs = {}
        for argument in options:
            value = self.create_value(argument["value"])
            key = argument["arg"]
            command_pairs[key] = value
        
        self.set_pair_keys(command_pairs)

    def create_value(self, value_str):
        possible_values = create_map()

        if value_str in possible_values:
            return Value(possible_values[value_str])
        else:
            return None

class CommandCenter:
    def __init__(self, json_object):
        self.command_blocks = []
        self.json_object = json_object

    def create_command(self, routine_key):
        sub_json_object = self.json_object[routine_key]

        command_blck = CommandBlock(routine_key)
        command_blck.to_pairs(sub_json_object)
        
        return command_blck

    def set_command(self, i, routine_key):
        command_blck = self.create_command(routine_key)
        self.command_blocks[i] = command_blck

    def add_command(self, routine_key):
        command_blck = self.create_command(routine_key)
        self.command_blocks.append(command_blck)

    def get_command(self, i):
        return self.command_blocks[i]

    def match_command(self, routine_key):
        for i in range(0, len(self.command_blocks)):
            if self.command_blocks[i].get_name() == routine_key:
                return i
        
        return -1