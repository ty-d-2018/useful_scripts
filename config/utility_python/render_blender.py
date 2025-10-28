from active.py import Activity

class RenderFrame(Activity):
    def __init__(self):
        super.__init__("render-scene")
        self.templates = {}

    def init_template(self):
        self.templates = {
            "#NUMBER"
        }