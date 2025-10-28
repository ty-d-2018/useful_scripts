
class Value:
    def __init__(self, name):
        self.value = None
        self.name = name
        self.is_set = False

    def set_value(self, value):
        self.value = value
        self.is_set = True 

    def is_value_set(self):
        return self.is_set

    def reverse_set(self):
        self.is_set = not self.is_set

    def get_value(self):
        return self.value

class Template:
    def __init__(self):
        self.tags = []

    def add_row(self, subject, value):
        self.tags.append([subject, value])

    def set_row(self, i, subject, value):
        self.tags[i] = [subject, value]

    def get_column(self, column_name):
        columns = []
        i = 0
        if column_name == "subject":
            i = 0
        elif column_name == "value":
            i = 1
        else:
            return None
        
        for rows in self.tags:
            columns.append(rows[i])
        
        return columns

    def get_row(self, i):
        row = [self.template[i][0], self.template[i][1]]

        return row

    def get_value(self, r):
        return self.template[r][1]

    def get_subject(self, r):
        return self.template[r][0]

    def set_all_values(self, literal_values):
        for i in range(0, len(self.tags)):
            self.tags[i][1] = literal_values[i]

    def set_value(self, i, literal_value):
        self.tags[i][1].set_value(literal_value)