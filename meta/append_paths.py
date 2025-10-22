from pathlib import Path
import json

def get_list(self):
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
                tag_add(keys[tag])
            elif tag == "#SUB":
                i = len(command)
                tag_add("sub")
            else:
                tag_add(tag)

        for sub_directory in sub:
            tag_set_index(i, sub_directory["folder"])
            export_add("".join(tag_get_whole()))
        

        return export_get_whole()