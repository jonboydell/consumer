from Factories import SteelFactory
import Resources as r
from unittest import TestCase


class TestMines(TestCase):
    def test_increment_output_on_tick(self):
      sf = SteelFactory('Steel Factory')
      sf.increment_input(r.coal)
      sf.increment_input(r.iron)
