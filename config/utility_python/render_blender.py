from standard_command.py import TemplateActivity, CommandBlock

from reader.py import ReadJson, ReadFile, create_file_path
from call.py import Volunteer

class RenderFrame:
    def __init__(self, json_src_file, blend_src_file, render_ouput_file):
        self.reader = ReadJson(json_src_file)
        self.blend_file = ReadFile(blend_src_file)
        self.render_path = ReadFile(render_output_file)
        self.template_activity = TemplateActivity()
        self.command_center = CommandCenter(self.reader.get_json())
        self.routine_key = "render-frame"
        self.volunteer = Volunteer()

    def setup_command_block(self):
        self.command_center.add_command(self.routine_key)
        subjects = ["background", "render-frame", "render-output"]
        values = []
        self.template_activity.set_keys_and_table()