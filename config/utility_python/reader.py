from pathlib import Path
import json

def create_file_path(file_path_str):
    full_path = Path(file_path_str).resolve()

class ReadFile:
    def __init__(self, file_path_str):
        self.file_path = create_file_path(file_path_str)
        self.content = ""

    def read_file(self):
        file_content = self.file_path.read_text()
    
    def is_content_empty(self):
        if self.content == "":
            return True

        return False

class ReadJson(ReadFile):
    def __init__(self, file_path_str):
        super().__init__(file_path_str)
        self.json_object = None

    def get_json(self):
        if self.is_content_empty():
            self.read_file()
        
        self.json_object = json.loads(self.content)
