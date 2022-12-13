# -*- coding: utf-8 -*-
backstage = "Backstage passes to a TAFKAL80ETC concert"
a_brie = "Aged Brie"
sulfuras = "Sulfuras, Hand of Ragnaros"

class GildedRose(object):
    def __init__(self, items):
        self.items = items
    def update_backstage(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item.quality += 1
        item.sell_in -= 1
        item.quality = min(item.quality, 50)
        
    def update_brie(self, item):
        if item.sell_in <= 0:
            item.quality += 2
        else:
            item.quality += 1
        item.sell_in -= 1
        item.quality = min(item.quality, 50)
            
        
    def update_other(self, item):
        if item.sell_in <= 0:
            item.quality -= 2
        else:
            item.quality -= 1
        item.sell_in -= 1
        item.quality = max(item.quality, 0)
        item.quality = min(item.quality, 50)
    
    def update_conjured(self, item):
        if item.sell_in <= 0:
            item.quality -= 4
        else:
            item.quality -= 2
        item.sell_in -= 1
        item.quality = max(item.quality, 0)
        item.quality = min(item.quality, 50)
    
    def update_quality(self):
        for item in self.items:
            if item.name[0:8] == "Conjured":
                self.update_conjured(item)
            elif item.name == backstage:
                self.update_backstage(item)
            elif item.name == a_brie:
                self.update_brie(item)
            elif item.name != sulfuras:
                self.update_other(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
