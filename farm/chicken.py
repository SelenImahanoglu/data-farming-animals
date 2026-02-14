from farm.animal import Animal

class Chicken(Animal):
    def __init__(self, gender):
        super().__init__()
        self.gender = gender # "female" (dişi) veya "male" (erkek)
        self.eggs = 0

    def talk(self):
        return "cluck cluck" if self.gender == "female" else "cock-a-doodle-doo"

    def feed(self):
        super().feed()       # Enerjiyi 1 artır
        if self.gender == "female":
            self.eggs += 2   # Sadece dişiler 2 yumurta üretir
