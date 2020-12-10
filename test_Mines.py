from Mines import IronMine
import Resources as r
from unittest import TestCase


class TestMines(TestCase):
    def test_increment_output_on_tick(self):
        im = IronMine('Iron Mine')
        i = 0
        while i < 5:
            self.assertFalse(r.iron in im.output)
            im.tick()
            i = i + 1
        self.assertTrue(r.iron in im.output)

    def test_increment_output(self):
        im = IronMine('Iron Mine')
        im.increment_output(r.iron)
        self.assertTrue(r.iron in im.output)

