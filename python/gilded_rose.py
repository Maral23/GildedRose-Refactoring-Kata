from item import ItemBuilder

class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()

    def create_item(self, name, days_left, quality):
        """Factory method using Builder pattern"""
        builder = ItemBuilder(name, days_left, quality)
        if name.startswith("Conjured"):
            builder.with_decorator("Conjured")
        return builder.build()