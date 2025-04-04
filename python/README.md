What we learned:

This assignment was a challenge in design, time management. At first, the messy code made it hard to understand and modify, but breaking things into smaller, reusable parts made everything much cleaner. Time pressure was definitely a factor. We thought we had enough time, but refactoring properly took more effort than expected. Planning before coding turned out to be really important.
Collaboration helped a lot. Talking through ideas made us spot better solutions and catch mistakes. 
One key takeaway was how small changes can have a big impact. Adding the new "GALA concert" backstage pass seemed simple, but making sure it worked smoothly showed why good design matters. Finally, coming up with another pattern at level 6 prove to be an exciting exercise.

Level 1:

Main goal was to refactor the `update_quality` method to make the code more organized. We separated the logic into smaller methods. And also renamed `sell_in` to `days_left` to improve clarity. 
⁃The `update_sell_in` method is now responsible for decreasing the `days_left` value,  excluding "Sulfuras" 
⁃The `update_item_quality` determines the item type and directs the process to the appropriate handling function. 
⁃`update_normal_item_quality` meant to reduce quality normally, with an additional reduction once the item has passed its expiry date.
⁃	 `update_aged_brie_quality  quality increases consistently and continues even after the expiration date
-`update_backstage_passes_quality` the quality increasing more quickly as the concert date approaches and dropping to zero once the concert has passed.
⁃Also, to test we updated test.py to cover various scenarios, to make sure the code behaves as expected for each type of item

Level 2:
Main goal was to implement the Strategy Pattern to replace the large if statement with separate strategy classes for each item type. This makes the code cleaner and more maintainable.
-We created individual strategy classes like AgedBrieStrategy, SulfurasStrategy, BackstagePassesStrategy, and NormalItemStrategy to handle item-specific behavior.
-The GildedRose class now uses a dictionary to map item names to their respective strategy classes and calls the appropriate strategy for each item.
-Tests were updated to cover various item types and ensure the correct behavior, like verifying that backstage passes increase in quality or that Sulfuras remains unchanged.


Level 3:
The goal was to transition from strategy classes to polymorphism( simplifying the code and removing unnecessary branching).
-turned Item into an abstract class and created specific subclasses for each item type (AgedBrie, Sulfuras, BackstagePasses, and NormalItem).
⁃Each subclass now implements its own update_quality method and has the behavior specific to that item.
⁃The GildedRose class directly works with item subclasses by calling their update_quality method without needing to check the item type.
⁃We also created a separate item.py file to define the Item class and its subclasses, keeping the code easier to maintain and not clutter the gilded_rose.py file.


Level 4: 
The goal was to introduce  Open/Closed Principle,where new behaviors can be added without modifying existing code and  introduce the Factory Method 
⁃Added the "Backstage passes to a GALA concert" item with specific behavior 
⁃Introduced a create_item method in the GildedRose class to instantiate the correct subclass based on the item's name (like AgedBrie, Sulfuras, and etc). This ensures that if we add more items in the future, we can do so without modifying the existing code in GildedRose, just need to add new subclasses and update the create_item method.

Level 5:
⁃The goal was to introduce the Decorator Pattern to modify behavior of existing items 
⁃Added Conjured" items that degrade in quality twice as fast as normal items.
⁃Maintained Open/Closed Principle (new modifications don’t require changes to existing classes).
⁃We added ConjuredItem as a decorator that wraps any existing Item (and doubles its quality degradation.
⁃Updated the Factory Method (create_item) to support "Conjured" items


Level 6:
The goal was to improve item creation by introducing the some other pattern. We chose  Builder Pattern for more flexible object construction.
•Added an ItemBuilder class to handle complex item creation with optional decorators.
•Replaced the growing if-elif chain in create_item() with a cleaner andmore maintainable builder.
•Enabled method chaining (with_decorator("Conjured")) for readable item configuration.
•Kept backward compatibilit. The original create_item() factory still works but now uses the builder internally


