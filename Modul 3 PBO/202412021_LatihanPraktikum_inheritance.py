class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        return f"Kendaraan: {self.merk} ({self.tahun})"

class Mobil(Kendaraan):
    def __init__(self, merk, tahun, jumlah_pintu):
        super().__init__(merk, tahun)
        self.jumlah_pintu = jumlah_pintu

    def info(self):
        return f"Mobil: {self.merk}, {self.jumlah_pintu} pintu ({self.tahun})"

# Instansiasi
k = Kendaraan("Yamaha", 2020)
m = Mobil("Toyota", 2022, 4)

print(k.info())
print(m.info())


# ==============================
# Tambahan sesuai perintah:
# Buat class Person dengan atribut nama dan umur
# ==============================

class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Person: {self.nama}, Umur: {self.umur}"


# Contoh penggunaan
p = Person("Budi", 30)
print(p.info())
