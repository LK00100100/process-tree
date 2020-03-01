from unittest import TestCase

from process_tree.process_tree.ProcessTree import ProcessTree


def double_func(input_val):
    return input_val * 2


def minus_two_func(input_val):
    return input_val - 2


class TestProcessTree(TestCase):

    def test_should_init_tree_correctly(self):
        # init tree
        num_op_nodes = 2
        init_val = 10
        process_tree = ProcessTree(num_op_nodes, init_val)
        process_tree.op_level_map[1].set_op(double_func)
        process_tree.op_level_map[2].set_op(minus_two_func)

        result = process_tree.recalc_tree()

        # ASSERT
        expected_val = 18
        self.assertEqual(expected_val, result)
