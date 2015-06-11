import unittest
from pyioc import IoCList

from collections import OrderedDict, Counter


class TestPyIoC(unittest.TestCase):

    def test_ordered_dict(self):

        container = IoCList()
        container.append(OrderedDict)
        container.append(Counter)

        class Foo(object):
            @container.inject_dependency(dic=dict)
            def __init__(self, dic):
                self.dic = dic
            def put(self, key, val):
                self.dic[key] = val

        foo = Foo()
        foo.put('a', 3)
        self.assertEqual(foo.dic.__class__, OrderedDict)

    def test_counter(self):

        container = IoCList()
        container.append(Counter)

        class Foo(object):
            @container.inject_dependency(dic=dict)
            def __init__(self, dic):
                self.dic = dic
            def put(self, key, val):
                self.dic[key] = val

        foo = Foo()
        foo.put('a', 3)
        self.assertEqual(foo.dic.__class__, Counter)



if __name__ == '__main__':
    unittest.main()
