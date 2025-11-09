from pathlib import Path
import json


class File:
    def __init__(self, file_path_str):
        self.file_path = File.create_file_path(file_path_str)
        self.content = ""
    
    @staticmethod
    def create_file_path(file_path_str):
        full_path = Path(file_path_str).resolve()
        return full_path

    def file_process(self):
        print(f"file path is: {str(self.file_path)}")
        self.content = self.file_path.read_text()
    
    def is_content_empty(self):
        if self.content == "":
            return True

        return False

    def get_file_string(self):
        return str(self.file_path)

    def get_parent_file_string(self):
        return str(self.file_path.parent)

    def get_parent_directory(self):
        file = File(self.get_parent_file_string())

        return file

    def get_file_path(self):
        return self.file_path

    def travel_and_get_file(self, sub_path):
        file = self.get_parent_directory()
        file_path = file.get_file_path()
        new_path = file_path / sub_path

        sub_file = File(str(new_path))

        return sub_file


class ReadFile(File):
    def __init__(self, file_path_str):
        super().__init__(file_path_str)
        self.file_process()

class BinaryFile(File):
    def __init__(self, file_path_str):
        super().__init__(file_path_str)
    
    @staticmethod
    def create_file_path(file_path_str):
        full_path = Path(file_path_str).resolve(strict=False)

    def file_process(self):
        pass

class ReadJson(ReadFile):
    def __init__(self, file_path_str):
        super().__init__(file_path_str)
        self.json_object = None

    def get_json(self):
        if self.is_content_empty():
            self.read_file()
        
        self.json_object = json.loads(self.content)

class WriteFile(File):
    def __init__(self, file_path_str, content):
        super().__init__(file_path_str)
        self.content = content

    def file_process(self):
        self.file_path.write_text(self.content)