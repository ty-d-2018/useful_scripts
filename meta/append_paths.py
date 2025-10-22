from pathlib import Path
import json

def get_list():
    command = []

    def append_to_command(value):
        command.append(value)

    def get_command(i):
        command[i]

    def set_command(i, value):
        command[i] = value

    def get_whole_command():
        return command

    return append_to_command, get_command, set_command, get_whole_command

class Source:
    def __init__(self, source_path, relative_path):
        self.path = (source_path / relative_path).resolve()
        self.content = ""

    def read_file(self):
        file_content = self.path.read_text()
        return file_content

    def read_and_set_content(self):
        self.content = self.read_file()

    def write_file(self):
        self.path.write_text(self.content)

    def append_file(self):
        with self.path.open(mode='a') as f:
            f.write(self.content)

    def get_content(self):
        return self.content

    def set_content(self, text):
        self.content = text

    def append_content(self, text, seperator=""):
        self.content = f"{self.content}{text}{seperator}"

    def is_in_file(self, query):
        file_content = self.read_file()
        if query in file_content:
            return True
        return False



class Script:
    def __init__(self, target_config=".bashrc"):
        self.script_path = Path(__file__).resolve().parent
        self.config = Source(self.script_path, "../config/home_bin_bash_rc.json")
        self.json = {}
        self.bash_rc = Source(Path.home(), target_config)
        self.keys = self.setup_keys()

    def read_json(self):
        self.config.read_and_set_content()
        self.json = json.loads(self.config.get_content())

    def write_bash_rc(self, commands):
        self.bash_rc.set_content("")
        for line in commands:
            self.bash_rc.append_content(line, "\n")

        if not self.bash_rc.is_in_file(self.bash_rc.get_content()):
            print("appending to .bash_rc")
            self.bash_rc.append_file()

    def setup_keys(self):
        return {
            "#QUOTE": "\"",
            "#SPACE": " ",
            "#BIN": "${HOME}/bin/github_repos",
            "#REPO": "useful_scripts",
        }
    
    def get_commands(self):
        if self.json is None:
            self.read_json()
        
        paths = self.json["paths"]
        tags = paths["exec_tag_line"]
        sub = paths["SUB"]
        i = 0

        tag_add, _, tag_set_index, tag_get_whole = get_list()
        export_add, _, _, export_get_whole = get_list()


        for tag in tags:
            if tag in self.keys:
                tag_add(self.keys[tag])
            elif tag == "#SUB":
                i = len(tag_get_whole())
                tag_add("sub")
            else:
                tag_add(tag)

        for sub_directory in sub:
            tag_set_index(i, sub_directory["folder"])
            export_add("".join(tag_get_whole()))
        

        return export_get_whole()

    def act(self):
        self.read_json()
        commands = self.get_commands()
        self.write_bash_rc(commands)

    
script = Script()
script.act()