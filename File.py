class File:
    """
    A file in the file system. Just contains text data
    """
    def __init__(self, name):
        self.name = ""
        self.data = ""

    def write(self, offset, data):
        """
        Writes data to the buffer starting at the desired offset. The buffer
        will be extended to the needed size.
        """
        # Check if the data buffer needs to grow
        if offset + len(data) > len(self.data):
            # Grow with spaces
            self.data = self.data + " " * (offset + len(data) - len(self.data))

        # Overwrite the desired area
        self.data = self.data[:offset] + data + self.data[offset+len(data):]

    def read(self, offset, length):
        """
        Reads data from the buffer starting at the desired offset up to the
        desired length. If the offset is larger than the file, then an empty
        string is returned
        """
        return self.data[offset:offset+length]
