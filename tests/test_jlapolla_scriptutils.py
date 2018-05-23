from   tests.common import TestCase
import jlapolla_scriptutils as mod


class TestOne(TestCase):

    def test_one(self):
        self.assertEqual(mod.one(), 1)
