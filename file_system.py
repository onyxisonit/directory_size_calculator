class File:
    def __init__(self, file_name, size):
        self.file_name = file_name
        self.size = size

class Dictionary:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subdirectories = []
        self.parent = None

    def add_subdirectory(self, subdir):
        subdir.parent = self
        self.subdirectories.append(subdir)

    def add_file(self, file):
        self.files.append(file)