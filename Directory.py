class Directory:
    """
    A directory node in the file system tree
    """

    def __init__(self, name, parent):
        self.subdirectories = {}
        self.files = {}

        self.name = name
        self.parent = parent

    def create_subdirectory(self, name):
        """
        Create a new subdirectory. Returns True if succeeded, returns
        False if there is already such a directory
        """
        if name in self.subdirectories:
            return False
        else:
            subdir = Directory(name, self)
            self.subdirectories[name] = subdir
            return True

    def get_subdirectory_names(self):
        """
        Returns a list of subdirectory names sorted
        in alphabetical order
        """
        return sorted(self.subdirectories.keys())

    def get_file_names(self):
        """
        Returns a list of file names sorted in alphabetical order
        """
        return sorted(self.files.keys())
