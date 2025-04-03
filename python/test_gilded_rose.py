# -*- coding: utf-8 -*-
import unittest
from gilded_rose import GildedRose, Item

class TestGildedRose(unittest.TestCase):

    def test_regular_item_quality_decreases(self):
        item = Item("Regular Item", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 9)
        self.assertEqual(item.days_left, 4)

    def test_regular_item_quality_decreases_after_days_left(self):
        item = Item("Regular Item", -1, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 8)

    def test_aged_brie_quality_does_not_exceed_50(self):
        item = Item("Aged Brie", 5, 49)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 50)
 
    def test_aged_brie_quality_increases(self):
        item = Item("Aged Brie", 10, 15)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.days_left, 9)
        self.assertEqual(item.quality, 16) 

    def test_backstage_passes_increase_quality(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 11)

    def test_backstage_passes_quality_drops_to_0_after_concert(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 0)

    def test_sulfuras_quality_does_not_change(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 80)



if __name__ == "__main__":
    unittest.main()

