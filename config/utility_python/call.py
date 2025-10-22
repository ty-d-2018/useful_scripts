import subprocess

class CallingCommand:
    def __init__(self, commandMap):
        self.commands = []
        for key, value in commandMap.items():
            tempC = []
            tempC.append(key)
            tempC.append(value)
            self.commands.append(tempC)
        
    def execute_command(self, c):
        return subprocess.run(c, capture_output=True, text=True, check=True)

    def run_all_commands(self):
        results = []
        for command in self.commands:
            results.append(self.execute_command(command))
        
        return results

    def run_a_command(self, i):
        result = self.execute_command(self.commands[i])

        return result

    def get_commands(self):
        return self.commands