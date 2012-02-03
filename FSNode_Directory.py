from FSException import FSException
from FSNode import FSNode

class FSNode_Directory(FSNode):
    """
    A directory node in the file system tree
    """
    def __init__(self, name, parent):
        FSNode.__init__(self, name, parent)

    def get_type(self):
        return "FSNODE_DIRECTORY"
