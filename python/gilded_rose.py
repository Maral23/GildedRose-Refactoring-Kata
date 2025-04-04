# -*- coding: utf-8 -*-

from item import AgedBrie, Sulfuras, BackstagePasses, NormalItem, GalaBackstagePasses

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()

    def create_item(self, name, days_left, quality): # Factory methid creates correct item type based on the item name
        if name == "Aged Brie":
            return AgedBrie(days_left, quality)
        elif name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(days_left, quality)
        elif name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePasses(days_left, quality)
        elif name == "Backstage passes to a GALA concert":
            return GalaBackstagePasses(days_left, quality)
        else:
            return NormalItem(name, days_left, quality)

