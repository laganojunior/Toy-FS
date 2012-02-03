from Directory import Directory

class Filesystem:
    """
    An implementation of a toy in-memory filesystem
    """

    def __init__(self):
        # Initalize the root directory
        self.root = Directory("", None)

        # Initialize the directory cursor to the root directory
        self.curr = self.root

    def create_directory(self, name):
        """
        Create a new subdirectory under the current directory
        """
        self.curr.create_subdirectory(name)

    def list_contents(self):
        """
        Returns a tuple of (list of subdirectories, list of files)
        under the current directory
        """
        return (self.curr.get_subdirectory_names(), self.curr.get_file_names())
