#unit test

import unittest
import app

class TestStringMethods(unittest.TestCase):
    def testStr(self):
        self.assertEqual(app.ex_func('aaaa'),'aaaa')
