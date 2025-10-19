from pathlib import Path
import json

class Script:
    def __init__(self):
        self.source = Path(__file__).resolve().parent
        self.config = (d / "../config/home_bin_bash_rc.json")
        self.json = None
        self.bash_rc = (Path.home() / ".bashrc").resolve()

    def read_json(self):
        with open(self.config, 'r') as jf:
            self.json = json.load(jf)

    def write_bash_rc(self, commands):
        with open(self.bash_rc, 'a') as bf:
            for line in commands:
                bf.write(line)
    
    def get_commands(self):
        if self.json is None:
            self.read_json()
        
        paths = self.json["paths"]
        tags = paths["exec_tag_line"]
        sub = paths["SUB"]
        command = []
        i = 0
        
        keys = {
            "#QUOTE": "\"",
            "#SPACE": "",
            "#BIN": "$HOME/bin",
            "#REPO": "useful_scripts",
        }

        for tag in tags:
            if tag in keys:
                command.append(keys[tag])
            elif tag == "#SUB":
                i = len(command)
                command.append("sub")
            else:
                command.append(tag)

        export_strings = []

        for sub_directory in sub:
            command[i] = sub_directory["folder"]
            export_strings.append(command)
        

        return export_strings