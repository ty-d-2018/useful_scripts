import argparse

class Argument:
    def __init__(self, tags):
        self.param_keys = argparse.ArgumentParser()

        for key, value in tags.items():
            self.param_keys.add_argument(key, type=value)

    def get_option(self, name):
        option_value = getattr(self.param_keys, name)