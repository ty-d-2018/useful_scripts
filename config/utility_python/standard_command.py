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

class TemplateActivity(Activity):
    def __init__(self):
        super().__init__("template-activity")
        self.template = Template()
        self.keys = {}

    def set_table(self, subjects, values):
        for i in range(0, len(subjects)):
            self.template.add_row(subjects[i], values[i])

    def set_keys(self):
        column = self.template.get_column("subject")
        for i in range(0, len(column)):
            self.keys[column[i]] = i

    def set_keys_and_table(self, subjects, values):
        self.set_table(subjects, values)
        self.set_keys()

    def read_block(self, name, block):
        block.set_value(self.template.get_value(name))

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
            if len(key) == 1:
                key = f"-{key}"
            else:
                key = f"--{key}"
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