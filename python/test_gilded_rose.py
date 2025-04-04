# -*- coding: utf-8 -*-
import unittest
from gilded_rose import GildedRose
from item import ItemBuilder, NormalItem, ConjuredItem

class TestGildedRose(unittest.TestCase):
    def test_builder_creates_conjured_item(self):
        item = (ItemBuilder("Mana Cake", 5, 10)
               .with_decorator("Conjured")
               .build())
        self.assertTrue(isinstance(item, ConjuredItem))
        self.assertEqual(item.name, "Conjured Mana Cake")

    def test_conjured_item_degrades_twice_as_fast(self):
        # Using builder pattern
        item = (ItemBuilder("Normal Item", 5, 10)
               .with_decorator("Conjured")
               .build())
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 8)
        self.assertEqual(item.days_left, 4)

    def test_conjured_item_degrades_twice_as_fast_after_expiry(self):
        # Using builder pattern
        item = (ItemBuilder("Normal Item", 0, 10)
               .with_decorator("Conjured")
               .build())
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 6)
        self.assertEqual(item.days_left, -1)

if __name__ == "__main__":
    unittest.main()

