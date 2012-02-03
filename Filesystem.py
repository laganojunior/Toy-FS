from FSNode_Directory import FSNode_Directory
from FSNode_File import FSNode_File
from FSException import FSException

class Filesystem:
    """
    An implementation of a toy in-memory filesystem
    """

    def __init__(self):
        # Initalize the root directory
        self.root = FSNode_Directory("", None)

        # Initialize the directory cursor to the root directory
        self.curr = self.root

    def create_directory(self, name):
        """
        Create a new subdirectory under the current directory
        """
        newdir = FSNode_Directory(name, self.curr)
        self.curr.add_child(name, newdir)

    def list_contents(self):
        """
        Returns a tuple of (list of subdirectories, list of files)
        under the current directory
        """
        contents = sorted(self.curr.get_children().items())
        directories = []
        files = []

        for (name, node) in contents:
            node_type = node.get_type()

            if node_type == "FSNODE_DIRECTORY":
                directories.append(name)
            elif node_type == "FSNODE_FILE":
                files.append(name)
            else:
                raise FSException("Unknown node type %s" % node_type)

        return (directories, files)

    def write_to_file(self, name, offset, data):
        """
        Writes data to a file in the current directory. If the file does not
        exist, then it will be created.
        """
        # Check if the name exists
        if self.curr.child_exists(name):
            node = self.curr.get_child(name)
            # If it isn't a file, then throw an error
            if node.get_type() != "FSNODE_FILE":
                raise FSException("Target %s is not a file" % name)
        else:
        # If it doesn't exist, make it
            node = FSNode_File(name, self.curr)
            self.curr.add_child(name, node)

        node.write(offset, data)

    def read_from_file(self, name, offset, length):
        """
        Reads from data from a file starting from the desired offset. If the
        file does not exist, this throws a FSException
        """
        if not self.curr.child_exists(name):
            raise FSException("File %s doesn't exist" % name)

        node = self.curr.get_child(name)
        if node.get_type() != "FSNODE_FILE":
            raise FSException("Target %s is not a file" % name)

        return node.read(offset, length)

    def rename(self, name, newname):
        """
        Rename a node
        """
        self.curr.rename_child(name, newname)

    def resolve_path(self, path):
        """
        Returns the directory corresponding to the path string relative to the
        current directory. Raises an FSException on an error.
        """
        if path == "":
            return self.curr

        # check if the path starts with /, then it is absolute and should start
        # root
        cursor = self.curr
        if path[0] == "/":
            cursor = self.root
            path = path[1:]

        dirs = path.split("/")

        for dirname in dirs:
            if dirname == "":
                continue

            if dirname == "..": # Parent
                p = cursor.get_parent()
                if p is not None:
                    # If the node has no parent,
                    # then it is the root. Otherwise,
                    # go up one level
                    cursor = p
                continue

            if not cursor.child_exists(dirname):
                raise FSException("Directory %s doesn't exist" % dirname)

            next_node = cursor.get_child(dirname)
            if next_node.get_type() != "FSNODE_DIRECTORY":
                raise FSException("Target %s is not a directory" % dirname)

            cursor = next_node

        return cursor

    def change_curr(self, path):
        """
        Changes the current directory
        """
        self.curr = self.resolve_path(path)

    def get_working_path(self):
        """
        Returns the current working path
        """
        return self.curr.pwd()

    def move(self, name, path, delete=True):
        """
        Moves a node
        """
        # Check the node exists
        if not self.curr.child_exists(name):
            raise FSException("Source %s doesn't exist" % name)

        target = self.resolve_path(path)

        if target.child_exists(name):
            raise FSException("Target name %s already exists in target location" % name)

        # Move the node by deleting it and recreating it
        node = self.curr.get_child(name)
        if delete:
            self.curr.delete_child(name)
        target.add_child(name, node)

    def delete(self, name):
        """
        Delete a node
        """
        self.curr.delete_child(name)

    def copy(self, name, path):
        """
        Copies a node
        """
        # Perform the move without the delete
        self.move(name, path, False)
