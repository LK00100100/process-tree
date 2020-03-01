from process_tree.process_tree.InitNode import InitNode
from process_tree.process_tree.OpNode import OpNode


class ProcessTree:
    """
    Stores operations and values
    """

    def __init__(self, num_op_nodes, initial_node_val):
        """
        :param initial_node_val: The first InitialNode's value
        :param num_op_nodes: The number of OpNodes to have
        :type initial_node_val: int
        :type num_op_nodes: int
        """
        # there is one OpNode per level.
        # the lowest OpNode is level 1.
        # map[level_num] => OpNode
        self.op_map = {}  # type: dict[int, OpNode]

        if num_op_nodes < 0:
            raise ValueError("Number of op nodes must be > 0")

        self.__init_op_nodes(num_op_nodes, initial_node_val)

        self.root_op_node = self.op_map[num_op_nodes]  # type OpNode

    def __init_op_nodes(self, num_op_nodes, initial_node_val):
        """
        Creates one OpNode per level
        :param num_op_nodes:
        :param initial_node_val: The InitNode val
        :return:
        """

        # first OpNode
        init_val_node = InitNode(initial_node_val)
        first_op_node = OpNode(init_val_node)
        self.op_map[1] = first_op_node

        prev_op_node = first_op_node

        # more OpNodes
        for i in range(1, num_op_nodes):
            op_node = OpNode(prev_op_node)
            self.op_map[i + 1] = op_node

            prev_op_node = op_node

    def parse_json(self, json_path):
        """
        Turns a specific json file and turns it into a tree

        Check unit tests.
        :param json_path: full path
        :type json_path: str
        :return:
        """
        raise NotImplementedError("maybe not needed")

    def recalc_tree(self):
        """
        Recalculates the entire tree
        :return:
        """
        return self.root_op_node.calculate_result()

    def print_tree(self):
        """
        Print an actual tree?
        Print a list?
        :return:
        """
        raise NotImplementedError("REEEE")
