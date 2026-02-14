from farm.animal import Animal

class Cow(Animal):
    def __init__(self):
        super().__init__() # Ebeveyn sınıfın energy=0 özelliğini başlatır
        self.milk = 0      # İneğe özel başlangıç süt miktarı

    def talk(self):
        return "moo"

    def feed(self):
        super().feed()     # Animal sınıfındaki energy += 1 işlemini yapar
        self.milk += 2     # İnek her beslendiğinde 2 litre süt üretir
