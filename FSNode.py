class FSNode:
    """
    A generic node in the filesystem. Specific nodes should derive from this
    class.
    """
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = {}

    def get_type(self):
        """
        Returns the type of this node. Deriving classes should override this
        """
        return "FSNODE_GENERIC"

    def add_child(self, name, node):
        """
        Adds a child. If the target node already exists, an FSException is
        raised
        """
        if name in self.children:
            raise FSException("Target %s already exists" % name)
        self.children[name] = node

    def delete_child(self, name):
        """
        Deletes a child. If the node doesn't already exist, then False is
        returned. Otherwise, returns True
        """
        if name not in self.children:
            return False
        else:
            del self.children[name]

    def rename_child(self, name, newname):
        """
        Renames a child node. If the node doesn't already exists,
        or a child of the target name already exists, then an FSException is
        thrown.
        """
        if name not in self.children:
            raise FSException("Source %s doesn't exist" % name)

        if newname in self.children:
            raise FSException("Target %s already exists" % newname)

        node = self.children[name]
        node.name = newname
        del self.children[name]
        self.children[newname] = node

    def child_exists(self, name):
        """
        Returns wheter a child node of the given name already exists
        """
        return name in self.children

    def get_child(self, name):
        """
        Returns a node for the given name. If it doesn't exist,
        None is returned
        """
        if name in self.children:
            return self.children[name]
        else:
            return None

    def get_children(self):
        """
        Returns a dictionary mapping names to children
        """
        return self.children

    def pwd(self):
        """
        Returns the path from the root to this node
        """
        if self.parent is None:
            return "/"
        else:
            return self.parent.pwd() + self.name + "/"

    def get_parent(self):
        """
        Returns the parent node
        """
        return self.parent
