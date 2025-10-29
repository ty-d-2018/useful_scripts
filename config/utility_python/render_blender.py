from standard_command.py import TemplateActivity, CommandBlock

from reader import ReadJson

class RenderFrame:
    def __init__(self, json_src_file):
        self.reader = ReadJson(json_src_file)
        self.command_center = CommandCenter(self.reader.get_json())
        self.routine_key = "render-frame"

    def setup_command_block(self):
        self.command_center.add_command(self.routine_key)