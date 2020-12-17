from Factories import SteelFactory
import Resources as r
from unittest import TestCase


class TestFactories(TestCase):
    def test_meets_production_threshold(self):
        sf = SteelFactory('Steel Factory')

        sf.increment_input(r.coal)
        sf.increment_input(r.iron)
        self.assertTrue(sf.meets_production_threshold())

        sf.decrement_input(r.coal)
        self.assertFalse(sf.meets_production_threshold())

        sf.decrement_input(r.iron)
        self.assertFalse(sf.meets_production_threshold())

        sf.increment_input(r.iron)
        self.assertFalse(sf.meets_production_threshold())

        sf.increment_input(r.coal)
        self.assertTrue(sf.meets_production_threshold())

    def test_tick(self):
        sf = SteelFactory('Steel Factory')

        sf.increment_input(r.coal)
        sf.increment_input(r.iron)
        self.assertTrue(sf.meets_production_threshold())

        sf.tick()
        self.assertTrue(sf.is_consuming)
        self.assertTrue(0 == sf.input[r.coal] and 0 == sf.input[r.iron] and 0 == sf.output[r.steel])

        sf.tick()
        self.assertTrue(sf.is_consuming)
        self.assertTrue(0 == sf.input[r.coal] and 0 == sf.input[r.iron] and 0 == sf.output[r.steel])

        sf.tick()
        self.assertTrue(sf.is_consuming)
        self.assertTrue(0 == sf.input[r.coal] and 0 == sf.input[r.iron] and 0 == sf.output[r.steel])

        sf.tick()
        self.assertTrue(sf.is_consuming)
        self.assertTrue(0 == sf.input[r.coal] and 0 == sf.input[r.iron] and 0 == sf.output[r.steel])

        sf.tick()
        self.assertFalse(sf.is_consuming)
        self.assertTrue(0 == sf.input[r.coal] and 0 == sf.input[r.iron] and 1 == sf.output[r.steel])
