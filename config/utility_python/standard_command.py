

class CommandBlock(Blocks):
    def __init__(self):
        super().__init__()
        self.template = Template()

    def init_template(self, json_object):
        options = json_object["options"]
        for argument in options:
            value = self.create_value(argument["value"])
            template.add_row(argument["arg"], value)

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

    def create_blocks(self,)