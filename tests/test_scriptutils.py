from   tests.common import TestCase
import scriptutils as s


class TestOne(TestCase):

    def test_one(self):
        self.assertEqual(s.one(), 1)
