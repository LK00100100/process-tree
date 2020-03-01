class ProcessNode:
    """
    This is an abstract base node for the ProcessTree
    """

    def __init__(self):
        pass

    def calculate_result(self):
        """
        The implementing node will calculate a result
        however they want
        :return:
        """
        raise NotImplementedError()

