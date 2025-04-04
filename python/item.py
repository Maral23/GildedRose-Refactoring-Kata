from abc import ABC, abstractmethod
# abstract class and its subclasses
class Item(ABC):
    def __init__(self, name, days_left, quality):
        self.name = name
        self.days_left = days_left
        self.quality = quality

    @abstractmethod
    def update_quality(self):
        pass


class ItemBuilder:
    """Builder pattern for creating items with optional decorators"""
    def __init__(self, name, days_left, quality):
        self.name = name
        self.days_left = days_left
        self.quality = quality
        self.decorators = []

    def with_decorator(self, decorator_name):
        """Add a decorator to be applied during build()"""
        self.decorators.append(decorator_name)
        return self  # Enable method chaining

    def build(self):
        """Construct the final item with all decorators applied"""
        # Create base item
        if self.name == "Aged Brie":
            item = AgedBrie(self.name, self.days_left, self.quality)
        elif self.name == "Sulfuras, Hand of Ragnaros":
            item = Sulfuras(self.name, self.days_left, self.quality)
        elif self.name == "Backstage passes to a TAFKAL80ETC concert":
            item = BackstagePasses(self.name, self.days_left, self.quality)
        elif self.name == "Backstage passes to a GALA concert":
            item = GalaBackstagePasses(self.name, self.days_left, self.quality)
        else:
            item = NormalItem(self.name, self.days_left, self.quality)

        # Apply decorators in order
        for decorator in self.decorators:
            if decorator == "Conjured":
                item = ConjuredItem(item)
        return item

class ConjuredItem(Item):
    """Decorator that makes items degrade twice as fast"""
    def __init__(self, item):
        self.item = item
        self.name = f"Conjured {item.name}"
        self.days_left = item.days_left
        self.quality = item.quality

    def update_quality(self):
        self.item.update_quality()  # First degradation
        if self.item.quality > 0:
            self.item.quality -= 1
            if self.item.days_left < 0 and self.item.quality > 0:
                self.item.quality -= 1
        
        # Sync state
        self.quality = self.item.quality
        self.days_left = self.item.days_left



class AgedBrie(Item):
    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
        self.days_left -= 1
        if self.days_left < 0 and self.quality < 50:
            self.quality += 1


class Sulfuras(Item):
    def update_quality(self):
        pass  # No change


class BackstagePasses(Item):
    def update_quality(self):
        if self.days_left <= 0:
            self.quality = 0
        elif self.days_left < 6:
            if self.quality < 50:
                self.quality += 3
        elif self.days_left < 11:
            if self.quality < 50:
                self.quality += 2
        else:
            if self.quality < 50:
                self.quality += 1
        self.days_left -= 1


class GalaBackstagePasses(Item):
    def update_quality(self):
        if self.days_left <= 0:
            self.quality = 0
        elif self.days_left <= 5:
            if self.quality < 50:
                self.quality += 4
        elif self.days_left <= 10:
            if self.quality < 50:
                self.quality += 3
        elif self.days_left > 10:
            if self.quality < 50:
                self.quality += 2
        self.days_left -= 1


class NormalItem(Item):
    def update_quality(self):
        if self.quality > 0:
            self.quality -= 1
        self.days_left -= 1
        if self.days_left < 0 and self.quality > 0:
            self.quality -= 1