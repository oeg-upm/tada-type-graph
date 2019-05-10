import unittest
import json
#import type_graph

test_graph_file = "test_wrestlers.json"


class TestGraph(unittest.TestCase):

    def test_load_graph(self):
        """
        :return:
        """
        g = type_graph.TypeGraph()
        g.load_from_file(test_graph_file)
        self.assertEqual(len(g.roots), 5)


if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    project_dir = path.dirname(path.dirname(path.abspath(__file__)))
    sys.path.append(project_dir)
    import type_graph
    test_graph_file = path.join(project_dir, 'tests', test_graph_file)

if __name__ == '__main__':
    unittest.main()