from process_tree.process_tree.ProcessNode import ProcessNode


class ResultNode(ProcessNode):
    """
    This node is used by OpNode to hold a value
    TODO: can we combine this and OpNode?
    """

    def __init__(self):
        ProcessNode.__init__(self)
        self.val = None

    def set_value(self, val):
        self.val = val

    def calculate_result(self):
        return self.val
