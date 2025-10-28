

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
        possible_values = {
            "#FILENAME": Value("file-path"),
            "#NUMBER": Value("numerial"),
            "#DIRECTORY": Value("directory-path")
        }

        if value_string in possible_values:
            return possible_values[value_string]
        else:
            return None