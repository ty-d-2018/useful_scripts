from pathlib import Path
import json

class Script:
    def __init__(self):
        self.source = Path(__file__).resolve().parent
        self.config = (d / "../config/home_bin_bash_rc.json")
        self.json = {}
        self.bash_rc = (Path.home() / ".bashrc").resolve()
        self.keys = self.setup_keys()

    def read_json(self):
        with open(self.config, 'r') as jf:
            self.json = json.load(jf)

    def write_bash_rc(self, commands):
        with open(self.bash_rc, 'a') as bf:
            for line in commands:
                bf.write(line)

    def setup_keys(self):
        return {
            "#QUOTE": "\"",
            "#SPACE": "",
            "#BIN": "$HOME/bin",
            "#REPO": "useful_scripts",
        }

    def get_command(self):
        command = []

        def append_to_command(value):
            nonlocal command.append(value)

        def get_command(i):
            nonlocal command[i]

        def set_command(i, value):
            nonlocal command[i] = value

        def get_whole_command():
            return nonlocal command

        return append_to_command, get_command, set_command, get_whole_command
    
    def get_commands(self):
        if self.json is None:
            self.read_json()
        
        paths = self.json["paths"]
        tags = paths["exec_tag_line"]
        sub = paths["SUB"]
        command = []
        i = 0

        add, get_index, set_index, get_whole = self.get_command()

        for tag in tags:
            if tag in self.keys:
                add(keys[tag])
            elif tag == "#SUB":
                i = len(command)
                add("sub")
            else:
                add(tag)

        export_strings = []

        for sub_directory in sub:
            set_index(i, sub_directory["folder"])
            export_strings.append("".join(get_whole()))
        

        return export_strings