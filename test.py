import unittest
import app

class TesterClass(unittest.TestCase):

    def test_rev_word(self):
        self.assertEqual(app.rev_word("this is a unit test"),"test unit a is this")

