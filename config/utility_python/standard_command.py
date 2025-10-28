from block.py import Blocks
from active.py import Activity
from template.py import Template

def create_map():
    arg_map = {
        "#FILENAME": "file-path",
        "#NUMBER": "numerial",
        "#DIRECTORY": "directory-path"
    }

    return arg_map

class TemplateActivity(Activity):
    def __init__(self):
        super().__init__("template-activity")
        self.template = Template()
        self.keys = {}

    def set_table(self, subjects, values):
        for i in range(0, len(subjects)):
            template.add_row(subjects[i], values[i])

    def set_keys(self):
        arg_map = {}
        column = self.template.get_column("subject")
        for i in range(0, len(column)):
            self.arg_map[column[i]] = i

    def set_keys_and_table(self, subjects, values):
        self.set_table(subjects, values)
        self.set_keys()

    def read_block(self, name, block):
        blocks.set_value(self.template.get_value(self.keys[name]))

class CommandBlock(Blocks):
    def __init__(self):
        super().__init__()

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
            commnad_pairs[key] = value
        
        self.set_pair_keys(command_pairs)

    def create_value(self, value_str):
        possible_values = create_map()

        if value_string in possible_values:
            return Value(possible_values[value_string])
        else:
            return None

class CommandCenter:
    def __init__(self, json_object):
        self.command_blocks = []
        self.json_object = json_object

    def create_command(self, routine_key):
        sub_json_object = self.json_object[routine_key]

        command_blck = CommandBlock()
        command_blck.to_pairs(sub_json_object)
        
        return command_blck

    def set_command(self, i, routine_key):
        command_blck = self.create_command(routine_key)
        self.command_blocks[i] = command_blck

    def add_command(self, routine_key):
        command_blck = self.create_command(routine_key)
        self.command_blocks.append(command_blck)