from process_tree.process_tree.ProcessNode import ProcessNode


class InitNode(ProcessNode):
    """
    This is the bottom left most child of the ProcessTree
    This first thing used for the Tree's calculation
    """

    def __init__(self, val):
        ProcessNode.__init__(self)
        self.val = val

    def calculate_result(self):
        return self.val
