from process_tree.process_tree.ProcessNode import ProcessNode
from process_tree.process_tree.ResultNode import ResultNode


class OpNode(ProcessNode):
    """
    OpNode holds a function/operation
    Does calculations with child_op_node
    """

    def __init__(self, child_op_node):
        ProcessNode.__init__(self)
        self.op = None  # some function
        self.child_op_node = child_op_node   # type: ProcessNode
        self.result_node = ResultNode()

        # we don't want to recalc the same thing million times
        self.needs_recalc = True

    def set_op(self, some_function):
        """
        Sets the "op" to some_function.

        You may need to recalculate the tree.
        You may want to set a bunch of operations before doing a recalc.

        :param some_function:
        :type: function
        :return:
        """
        self.op = some_function

        self.needs_recalc = True

    def calculate_result(self):
        """
        Calculates child's results and then store the result in a result node
        :return: the result
        """
        if not self.needs_recalc:
            return self.result_node.val

        child_result = self.child_op_node.calculate_result()
        op_result = self.op(child_result)

        self.result_node.set_value(op_result)

        self.needs_recalc = False

        return op_result
