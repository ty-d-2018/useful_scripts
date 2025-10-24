
class Activity:
    def __init__(self, name):
        self.name = name
        self.tags = {}

    def get_label(self):
        return self.name

    def add_tag(self, key, value):
        self.tags[key] = value

    def set_tag(self, tags):
        self.tags = tags

    def reset_tags(self):
        self.tags = {}

    def read_block(self, name, block):
        print(f"I have the block named: {name}")

    def get_tags(self):
        return self.tags

    def send_tags(self, resolution):
        resolution.set_tags(self.get_tags())