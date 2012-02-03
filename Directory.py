from File import File

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

    def get_file(self, name):
        """
        Returns a file object for the given file name. If the file does not
        exist, None is returned
        """
        if name in self.files:
            return self.files[name]
        else:
            return None

    def create_file(self, name):
        """
        Creates a new empty file for the given filename. Returns True if
        successful. Returns False if the file already existed (the existing
        file is not overwritten)
        """

        if name in self.files:
            return False
        else:
            f = File(name)
            self.files[name] = f
            return True

    def file_exists(self, name):
        """
        Returns whether a file exists
        """
        return name in self.files
