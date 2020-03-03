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

        # OpNode or InitNode
        self.child_op_node = child_op_node  # type: ProcessNode
        self.result_node = ResultNode()
        self.parent = None  # type: OpNode

        # we don't want to recalc the same thing million times
        self.needs_recalc = True

    def get_result(self):
        return self.result_node.val

    def set_parent(self, parent):
        """
        Sets the parent node
        :type parent: ProcessNode
        """
        self.parent = parent

    def set_op(self, some_function):
        """
        Sets the "op" to some_function.

        You may want to recalculate the tree or call update_all()
        You may want to set a bunch of operations before doing a slow recalc.

        :param some_function: set this operator to this function
        :type: function
        :return:
        """
        self.op = some_function

        self.needs_recalc = True

    def set_op_and_update(self, some_function):
        """
        Sets "op" to some function and updates the results of this node and
        all the process nodes above it.
        :param some_function: set this operator to this function
        :return:
        """
        self.op = some_function

        self.update_all()

    def update_all(self):
        """
        Force updates this processNode's result and calls update_all on its
        parent ProcessNode
        :return:
        """
        self.needs_recalc = True

        self.calculate_result()

        if self.parent is not None:
            self.parent.update_all()

        self.needs_recalc = False

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

    def __str__(self):
        return "{} -> Result: {}".format(self.op.__name__, self.get_result())
