class Burung:
    def terbang(self):
        return "Burung terbang tinggi"

class Pesawat:
    def terbang(self):
        return "Pesawat lepas landas"

def uji_terbang(obj):
    print(obj.terbang())

# Duck typing dalam aksi
b = Burung()
p = Pesawat()

uji_terbang(b)
uji_terbang(p)

# Tambahan sesuai perintah
class Laptop:
    def nyalakan(self):
        return "Laptop dinyalakan"

class Smartphone:
    def nyalakan(self):
        return "Smartphone dinyalakan"

def tes_nyala(obj):
    print(obj.nyalakan())

# Demonstrasi duck typing
l = Laptop()
s = Smartphone()

tes_nyala(l)
tes_nyala(s)
