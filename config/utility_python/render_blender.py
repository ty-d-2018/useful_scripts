from config.utility_python.standard_command import ActivateCommand, CommandBlock
from config.utility_python.reader import ReadJson, ReadFile, BinaryFile
from config.utility_python.call import Volunteer, VolunteerActivity
from config.utility_python.active import Activity
from config.utility_python.blender import BlenderFiles

class RenderActivity(VolunteerActivity):
    def __init__(self):
        super().__init__("Blender Render CLI")

    def read_block(self, name, block):
        options.append(name)
        options.append(block)


class RenderFrame:
    def __init__(self, json_src_file, blend_src_file, render_output_file):
        self.blender_files = BlenderFiles()
        self.routine_key = "render-frame"
        self.volunteer = Volunteer()
        self.volunteer_activity = VolunteerActivity()
        self.command_block = CommandBlock()
        self.render_activity = VolunteerActivity()
        self.activate_command = None
        
        self.setup_blender_files(BinaryFile(blend_src_file), ReadJson(json_src_file), BinaryFile(render_output_file))

    def get_file_reader(self, key):
        return self.files[key]

    def get_json_object(self):
        return self.get_file_reader("json_fle").get_json()

    def get_options(self):
        json_object = self.get_json_object()
        return (json_object["render-frame"])["options"]

    def setup_blender_files(self, blender_file_handle, json_file_handle, output_file_handle):
        self.blender_files.setup_basic_files(blender_file_handle, output_file_handle)
        self.blender_files.insert_file("json_file", json_file_handle)

    def setup(self):
        self.setup_command()
        self.setup_activate_command()

    def setup_command(self):
        pairs = {}
        options = self.get_options()
        self.add_to_command_block(pairs, options)

    def setup_activate_command(self):
        values = []
        self.set_argument_values(values)
        self.init_activate_command(values, self.get_json_object())

    def init_activate_command(self, values, json_object):
        self.activate_command = ActivateCommand(values, json_object["render-frame"]["command-name"])

    def setup_subjects(self, subjects):
        for i in range(0, len(subjects)):
            if len(subjects[i]) > 1:
                subjects[i] = f"--{subjects[i]}"
            else:
                subjects[i] = f"-{subjects[i]}"
    
    def setup_activity_block(self):
        command_blocks = self.command_center.get_command(0)
        command_blocks.loop_blocks(self.template_activity.read_block)
        self.volunteer.add_block_layer(command_blocks, self.render_activity)

    def set_argument_values(self, values):
        self.values.append(self.get_file_reader("blend_file").get_file_string())
        self.values.append(1)
        self.values.append(self.get_file_reader("output_file").get_file_path())

    def loop_pairs(self, options, pairs):
        for option in options:
            arg = option["arg"]
            value = option["value"]
            pairs[arg] = value
    
    def add_to_command_block(self, pairs, options):
        self.loop_pairs(options, pairs)
        self.command_block.to_pairs(pairs)
    
    def transfer_to_activate_command(self):
        self.command_block.loop_blocks(self.activate_command.read_block)

    def transfer_command_to_volunteer(self):
        self.volunteer_activity.new_command(self.activate_command)

    def run_render(self):
        results = self.volunteer.run_all_layers()
        return results

    def print_results(self, results):
        for r in results:
            print(r.stdout)
