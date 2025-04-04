# -*- coding: utf-8 -*-
import unittest
from gilded_rose import GildedRose
from item import AgedBrie, Sulfuras, BackstagePasses, GalaBackstagePasses, NormalItem

class TestGildedRose(unittest.TestCase):

    def test_regular_item_quality_decreases(self):
        item = NormalItem("Regular Item", 5, 10) 
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 9)
        self.assertEqual(item.days_left, 4)

    def test_aged_brie_quality_increases(self):
        item = AgedBrie("Aged Brie", 10, 15)  
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 16)
        self.assertEqual(item.days_left, 9)

    def test_backstage_passes_increase_quality(self):
        item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 15, 10)  
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 11)

    def test_backstage_passes_quality_drops_to_0_after_concert(self):
        item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 0, 10)  # Instantiate BackstagePasses
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 0)
    
    # New test for Gala
    def test_gala_backstage_passes_quality_increases(self):
        item = GalaBackstagePasses("Backstage passes to a GALA concert", 12, 10)  
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 12)

    def test_sulfuras_quality_does_not_change(self):
        item = Sulfuras("Sulfuras, Hand of Ragnaros", 5, 80) 
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 80)
        self.assertEqual(item.days_left, 5)

if __name__ == "__main__":
    unittest.main()

