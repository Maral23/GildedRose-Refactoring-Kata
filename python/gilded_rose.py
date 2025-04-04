from item import AgedBrie, Sulfuras, BackstagePasses, GalaBackstagePasses, NormalItem, ConjuredItem

class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()

    def create_item(self, name, days_left, quality):
        item = None
        if name == "Aged Brie":
            item = AgedBrie(name, days_left, quality)
        elif name == "Sulfuras, Hand of Ragnaros":
            item = Sulfuras(name, days_left, quality)
        elif name == "Backstage passes to a TAFKAL80ETC concert":
            item = BackstagePasses(name, days_left, quality)
        elif name == "Backstage passes to a GALA concert":
            item = GalaBackstagePasses(name, days_left, quality)
        elif name.startswith("Conjured"): # since dont know which exactly item it is 
            base_item = NormalItem(name.replace("Conjured ", ""), days_left, quality)
            item = ConjuredItem(base_item)
        else:
            item = NormalItem(name, days_left, quality)
        return item