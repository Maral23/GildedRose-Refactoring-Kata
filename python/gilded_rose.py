# -*- coding: utf-8 -*-

class AgedBrieStrategy: # brie strategy
    def update_quality(self, item):
        if item.quality < 50:
            item.quality += 1
        item.days_left -= 1
        if item.days_left < 0 and item.quality < 50:
            item.quality += 1


class SulfurasStrategy: # sulfuras strategy
    def update_quality(self, item):
        pass  #nothing changes


class BackstagePassesStrategy:
    def update_quality(self, item):
        if item.days_left <= 0:  #occe the concert is over quality=0
            item.quality = 0
        elif item.days_left < 6:  # 5 days left =  quality x 3
            if item.quality < 50:
                item.quality += 3
        elif item.days_left < 11:  # 10 days left =  quality x 2
            if item.quality < 50:
                item.quality += 2
        else:  
            if item.quality < 50:
                item.quality += 1
        item.days_left -= 1  


class NormalItemStrategy: # any other item strategy
    def update_quality(self, item):
        if item.quality > 0:
            item.quality -= 1
        item.days_left -= 1
        if item.days_left < 0 and item.quality > 0:
            item.quality -= 1


class GildedRose(object): # using strategies
    def __init__(self, items):
        self.items = items
        self.strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassesStrategy()
        }

    def update_quality(self):
        for item in self.items:
            strategy = self.strategies.get(item.name, NormalItemStrategy())
            strategy.update_quality(item)



class Item:
    def __init__(self, name, days_left, quality):
        self.name = name
        self.days_left = days_left
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.days_left, self.quality)
