from standard_command.py import TemplateActivity, CommandBlock

from reader.py import ReadJson, ReadFile, create_file_path
from call.py import Volunteer, VolunteerActivity
from active.py import Activity

class RenderActivity(VolunteerActivity):
    def __init__(self):
        super.__init__("Blender Render CLI")

    def read_block(self, name, block):
        options.append(name)
        options.append(block)


class RenderFrame:
    def __init__(self, json_src_file, blend_src_file, render_ouput_file):
        self.reader = ReadJson(json_src_file)
        self.blend_file = ReadFile(blend_src_file)
        self.render_path = ReadFile(render_output_file)
        self.template_activity = TemplateActivity()
        self.command_center = CommandCenter(self.reader.get_json())
        self.routine_key = "render-frame"
        self.volunteer = Volunteer()
        self.render_activity = RenderActivity()

    def setup_command_block(self):
        self.command_center.add_command(self.routine_key)
        subjects = ["background", "render-frame", "render-output"]
        values = [self.blend_file.get_file_string(), 1, self.render_path.get_file_string()]
        self.template_activity.set_keys_and_table(subjects, values)

    def activity_block(self):
        command_blocks = self.command_center.get_command(0)
        command_blocks.loop_blocks(self.template_activity.read_block)
        self.volunteer.add_block_layer(command_blocks, self.render_activity)

    def run_render(self):
        results = self.volunteer.run_all_layers()
        for r in results:
            print(r.stdout)