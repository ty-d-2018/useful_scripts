
class BlenderFiles:
    def __init__(self):
        self.files = {}
    
    def insert_file(self, operation_name, file_handle):
        self.files[operation_name] = file_handle

    def get_file_reader(self, key):
        self.files[key]

    def setup_basic_files(self, blend_file_handle, output_file_handle):
        self.files["blend_file"] = blend_file_handle
        self.files["output_file"] = output_file_handle