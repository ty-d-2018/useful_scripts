from utility_python.render_python import RenderFrame

def create_render_frame(json_src_file, blend_src_file, render_output_file):
    render_frame = RenderFrame(json_src_file, blender_src_file, render_output_file)
    
    render_frame.setup_command_block()

def run_render(render_frame):
    render_frame.activity_block()
    render_frame.run_render()


def launch():
    render_frame = create_render_frame()
    run_render(render_frame)
