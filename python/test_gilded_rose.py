# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

backstage = "Backstage passes to a TAFKAL80ETC concert"
a_brie = "Aged Brie"
sulfuras = "Sulfuras, Hand of Ragnaros"

class GildedRoseTest(unittest.TestCase):
    def test_existentes(self):
        items = [
            Item("Zanahoria", 10, 5),   #decremento de 1 unidad
            Item("Tomate", 0, 4),       #decremento de 2 unidades
            Item("Cebolla", 2, 0),      #calidad no será negativa
            Item(a_brie, 4, 50),   #calidad no será mayor de 50
            Item(a_brie, 0, 40),   #calidad aumentará en 2 unidades
            Item(sulfuras, 50, 80), #ni calidad ni fecha cambiará
            Item(backstage, 15, 20), #calidad aumentará en 1 unidad
            Item(backstage, 10, 20), #calidad aumentará en 2 unidades
            Item(backstage, 5, 20),  #calidad aumentará en 3 unidades
            Item(backstage, 0, 20),  #calidad caerá a 0
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Zanahoria, 9, 4", items[0].__repr__())
        self.assertEqual("Tomate, -1, 2", items[1].__repr__())
        self.assertEqual("Cebolla, 1, 0", items[2].__repr__())
        self.assertEqual(a_brie + ", 3, 50", items[3].__repr__())
        self.assertEqual(a_brie + ", -1, 42", items[4].__repr__())
        self.assertEqual(sulfuras + ", 50, 80", items[5].__repr__())
        self.assertEqual(backstage + ", 14, 21", items[6].__repr__())
        self.assertEqual(backstage + ", 9, 22", items[7].__repr__())
        self.assertEqual(backstage + ", 4, 23", items[8].__repr__())
        self.assertEqual(backstage + ", -1, 0", items[9].__repr__())
    
    def test_nuevo(self):
        items = [
            Item("Conjured Mana Cake", 10, 5),   #decremento de 2 unidades
            Item("Conjured Mana Apple", 0, 4),    #decremento de 4 unidades
            Item("Conjured Mana Orange", 2, 0),   #calidad no será negativa
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake, 9, 3", items[0].__repr__())
        self.assertEqual("Conjured Mana Apple, -1, 0", items[1].__repr__())
        self.assertEqual("Conjured Mana Orange, 1, 0", items[2].__repr__())

        
if __name__ == '__main__':
    unittest.main()
