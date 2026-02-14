from farm.cow import Cow
from farm.chicken import Chicken

print("\n\n📝 Üçüncü Gün: Hayvanlar Konuşuyor")

# 1. Hayvanları oluştur
cow = Cow()
female_chicken = Chicken('female')
male_chicken = Chicken('male')

print(f"İnek {cow.talk()} diyor.")
print(f"Dişi tavuk {female_chicken.talk()} diyor.")
print(f"Erkek tavuk {male_chicken.talk()} diyor.")

print("\n\n📝 Dördüncü Gün: Hayvanları Besle")

# 1. Tüm hayvanlarını `animals` listesinde sakla
animals = [cow, female_chicken, male_chicken]

# 2. Her hayvan için `feed` yöntemini çağır (liste üzerinde bir döngü kullan)
for animal in animals:
    animal.feed()

# 4. Aşağıdaki 3 satırı yazdırın:
print(f"The cow produced {cow.milk} liters of milk")
print(f"The female chicken produced {female_chicken.eggs} eggs")
print(f"The male chicken produced {male_chicken.eggs} eggs")
