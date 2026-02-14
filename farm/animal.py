class Animal:
    def __init__(self):
        # Her hayvan sıfır enerji ile başlar
        self.energy = 0

    def feed(self):
        # Beslemek enerjiyi 1 artırır
        self.energy += 1
