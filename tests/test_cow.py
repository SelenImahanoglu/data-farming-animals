import unittest
from farm.cow import Cow

class TestCow(unittest.TestCase):
    def test_initialize_sets_milk_to_zero(self):
        # İnek ilk oluştuğunda sütü 0 olmalı
        self.assertEqual(Cow().milk, 0)

    def test_initialize_sets_energy_to_zero(self):
        # İnek ilk oluştuğunda enerjisi 0 olmalı
        self.assertEqual(Cow().energy, 0)

    def test_talk_returns_moo(self):
        # talk() metodu 'moo' dönmeli
        self.assertEqual(Cow().talk(), "moo")

    def test_feed_adds_energy(self):
        # Beslendiğinde Animal'dan gelen enerji 1 artmalı
        c = Cow()
        c.feed()
        self.assertEqual(c.energy, 1)

    def test_feed_adds_milk(self):
        # Beslendiğinde süt 2 artmalı
        c = Cow()
        c.feed()
        self.assertEqual(c.milk, 2)

    def test_feed_extends_method(self):
        # super().feed() kullanıldığı için hem enerji hem süt artmalı
        c = Cow()
        c.feed()
        self.assertTrue(c.energy == 1 and c.milk == 2)
