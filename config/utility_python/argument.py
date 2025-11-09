import argparse

class Argument:
    def __init__(self, tags):
        self.param_keys = None
        self.set_tags(tags)

    def get_option(self, name):
        argParse = self.get_parsed()
        option_value = getattr(argParse, name)
        return option_value

    def get_parsed(self):
        return self.param_keys.parse_args()

    def set_tags(self, tags):
        self.param_keys = argparse.ArgumentParser()

        for key, value in tags.items():
            self.param_keys.add_argument(key, type=value)