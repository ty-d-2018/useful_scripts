from utility_python.render_python import RenderFrame
from utility_python.reader import File
from pathlib import Path

def create_render_frame(json_src_file, blend_src_file, render_output_file):
    render_frame = RenderFrame(json_src_file, blender_src_file, render_output_file)
    
    render_frame.setup_command_block()

    return render_frame

def get_json_file_string(file_name):
    file = File(__file__)
    file = file.travel_and_get_file(file_name)

    return file.get_file_string()

def create_file_path(file_path):
    file = File(file_path)

    return file

def run_render(render_frame):
    render_frame.activity_block()
    render_frame.run_render()


def launch(blender_file_path, render_directory, render_file_name):
    json_path = get_json_file_string("blender.json")
    blender_src_file = create_file_path(blender_file_path).get_file_string()
    render_output_file = create_file_path(render_directory).travel_and_get_file(render_file_name).get_file_string()

    render_frame = create_render_frame(json_path, blender_file_src, render_output_file)
    run_render(render_frame)
