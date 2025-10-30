from pathlib import Path
import json


class File:
    def __init__(self, file_path_str):
        self.file_path = File.create_file_path(file_path_str)
        self.content = ""
    
    @staticmethod
    def create_file_path(file_path_str):
        full_path = Path(file_path_str).resolve()

    def file_process(self):
        self.content = self.file_path.read_text()
    
    def is_content_empty(self):
        if self.content == "":
            return True

        return False

    def get_file_string(self):
        return str(self.file_path)

class ReadFile(File):
    def __init__(self, file_path_str):
        super.__init__(file_path_str)
        self.file_process()

class ReadJson(ReadFile):
    def __init__(self, file_path_str):
        super().__init__(file_path_str)
        self.json_object = None

    def get_json(self):
        if self.is_content_empty():
            self.read_file()
        
        self.json_object = json.loads(self.content)

class WriteFile(File):
    def __init__(self):