# -*- coding: utf-8 -*-

from item import AgedBrie, Sulfuras, BackstagePasses, NormalItem

class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()
