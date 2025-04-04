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


class AgedBrie(Item):
    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
        self.days_left -= 1
        if self.days_left < 0 and self.quality < 50:
            self.quality += 1


class Sulfuras(Item):
    def update_quality(self):
        pass  # No change in quality or days_left


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
