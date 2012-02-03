from File import File
from FSException import FSException

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

    def get_subdirectory(self, name):
        """
        Returns a directory object for the given file name. If the dir does not
        exist, None is returned
        """
        if name in self.subdirectories:
            return self.subdirectories[name]
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
            f = File()
            self.files[name] = f
            return True

    def file_exists(self, name):
        """
        Returns whether a file exists
        """
        return name in self.files

    def rename_file(self, name, newname):
        """
        Renames a file. If the file doesn't exist or the target file already
        exists, then a FSException is thrown
        """
        if name not in self.files:
            raise FSException("File %s doesn't exist" % name)

        if newname in self.files:
            raise FSException("Target %s already exists" % newname)

        f = self.files[name]
        del self.files[name]
        self.files[newname] = f

    def subdirectory_exists(self, name):
        """
        Returns whether a subdirectory exists
        """
        return name in self.subdirectories

    def rename_subdirectory(self, name, newname):
        """
        Renames a subdirectory, If the subdirectory doesn't exist or the target
        name already exists, then a FSException is thrown.
        """
        if name not in self.subdirectories:
            raise FSException("Directory %s doesn't exist" % name)

        if newname in self.subdirectories:
            raise FSException("Target %s already exist" % newname)


        subdir = self.subdirectories[name]
        subdir.name = newname
        del self.subdirectories[name]
        self.subdirectories[newname] = subdir

    def get_parent(self):
        """
        Gets the parent of this directory
        """
        return self.parent

    def pwd(self):
        """
        Returns the working directory string
        """
        if self.parent is None:
            return "/"
        else:
            return self.parent.pwd() + self.name + "/"
