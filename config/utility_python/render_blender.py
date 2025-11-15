from config.utility_python.standard_command import ActivateCommand, CommandBlock

from config.utility_python.reader import ReadJson, ReadFile, BinaryFile
from config.utility_python.call import Volunteer, VolunteerActivity
from config.utility_python.active import Activity

class RenderActivity(VolunteerActivity):
    def __init__(self):
        super().__init__("Blender Render CLI")

    def read_block(self, name, block):
        options.append(name)
        options.append(block)


class RenderFrame:
    def __init__(self, json_src_file, blend_src_file, render_output_file):
        self.json_reader = ReadJson(json_src_file)
        self.blend_file = BinaryFile(blend_src_file)
        self.render_path = BinaryFile(render_output_file)
        self.routine_key = "render-frame"
        self.volunteer = Volunteer()
        self.volunteer_activity = VolunteerActivity()
        self.command_block = CommandBlock()
        self.render_activity = VolunteerActivity()
        self.activate_command = None

    def setup_command(self):
        json_object = self.json_reader.get_json()
        options = (json_object["render-frame"])["options"]
        pairs = {}
        for option in options:
            arg = option["arg"]
            value = option["value"]
            pairs[arg] = value
        self.command_block.to_pairs(pairs)

    def setup_activate_command(self):
        values = []
        self.values.append(self.blend_file.get_file_string())
        self.values.append(1)
        self.values.append(self.render_path.get_file_path())

        json_object = self.json_reader.get_json()
        command_call = json_object["render-frame"]["command-name"]

        self.activate_command = ActivateCommand(values, command_call)

    def transfer_to_activate_command(self):
        self.command_block.loop_blocks(self.activate_command.read_block)

    def transfer_command_to_volunteer(self):
        self.volunteer_activity.new_command(self.activate_command)

    def activity_block(self):
        command_blocks = self.command_center.get_command(0)
        command_blocks.loop_blocks(self.template_activity.read_block)
        self.volunteer.add_block_layer(command_blocks, self.render_activity)

    def run_render(self):
        results = self.volunteer.run_all_layers()
        for r in results:
            print(r.stdout)

    def setup_subjects(self, subjects):
        for i in range(0, len(subjects)):
            if len(subjects[i]) > 1:
                subjects[i] = f"--{subjects[i]}"
            else:
                subjects[i] = f"-{subjects[i]}"