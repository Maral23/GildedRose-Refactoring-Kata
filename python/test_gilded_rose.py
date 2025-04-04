# -*- coding: utf-8 -*-
import unittest
from gilded_rose import GildedRose
from item import AgedBrie, Sulfuras, BackstagePasses, GalaBackstagePasses, NormalItem, ConjuredItem

class TestGildedRose(unittest.TestCase):
    # New test for Conjured
    def test_conjured_item_degrades_twice_as_fast(self):
        normal_item = NormalItem("Normal Item", 5, 10)
        conjured_item = ConjuredItem(normal_item)
        gilded_rose = GildedRose([conjured_item])
        gilded_rose.update_quality()
        self.assertEqual(conjured_item.quality, 8)   # since expires twice as fast
        self.assertEqual(conjured_item.days_left, 4)

    def test_conjured_item_degrades_twice_as_fast_after_expiry(self):
        normal_item = NormalItem("Normal Item", 0, 10)
        conjured_item = ConjuredItem(normal_item)
        gilded_rose = GildedRose([conjured_item])
        gilded_rose.update_quality()
        self.assertEqual(conjured_item.quality, 6)  # since expires twice as fast
        self.assertEqual(conjured_item.days_left, -1)


if __name__ == "__main__":
    unittest.main()

