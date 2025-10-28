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
        arg_map = create_map()
        column = self.template.get_column("subject")
        for i in range(0, len(column)):
            if column[i] in arg_map:
                self.keys[column[i]] = i

    def set_keys_and_table(self, subjects, values):
        self.set_table(subjects, values)
        self.set_keys()

    def read_block(self, name, block):
        blocks = self.template.get_value(self.keys[name])

class CommandBlock(Blocks):
    def __init__(self):
        super().__init__()

    def to_pairs(self, json_object):
        options = json_object["options"]
        command_pairs = {}
        for argument in options:
            value = self.create_value(argument["value"])
            commnad_pairs[argument["arg"]] = value
        
        self.set_pair_keys(command_pairs)

    def create_value(self, value_str):
        possible_values = create_map()

        if value_string in possible_values:
            return Value(possible_values[value_string])
        else:
            return None