class Hewan:
    def bersuara(self):
        return "Hewan bersuara"

class Kucing(Hewan):
    def bersuara(self):
        return "Meow!"

class Anjing(Hewan):
    def bersuara(self):
        return "Woof!"

hewan_list = [Hewan(), Kucing(), Anjing()]

for h in hewan_list:
    print(h.bersuara())

# Tambahan sesuai perintah
class Bentuk:
    def luas(self):
        return 0

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

class Lingkaran(Bentuk):
    def __init__(self, r):
        self.r = r

    def luas(self):
        return 3.14 * self.r * self.r

# Demonstrasi pemanggilan method luas()
p = Persegi(4)
l = Lingkaran(3)

print("Luas Persegi:", p.luas())
print("Luas Lingkaran:", l.luas())
