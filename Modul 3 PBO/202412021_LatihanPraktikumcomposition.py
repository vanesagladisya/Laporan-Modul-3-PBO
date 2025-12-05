class Mesin:
    def __init__(self, jenis):
        self.jenis = jenis

    def hidupkan(self):
        return f"Mesin {self.jenis} hidup"

class Mobil:
    def __init__(self, merk, mesin):
        self.merk = merk
        self.mesin = mesin  # Composition

    def info(self):
        return f"Mobil {self.merk} dengan {self.mesin.hidupkan()}"

# Tambahan sesuai perintah
class Penulis:
    def __init__(self, nama):
        self.nama = nama

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis  # Composition

    def info(self):
        return f"Buku '{self.judul}' ditulis oleh {self.penulis.nama}"

# Instansiasi
mesin = Mesin("Bensin")
mobil = Mobil("Honda", mesin)
print(mobil.info())

# Demonstrasi composition Buku–Penulis
penulis = Penulis("Vanesa")
buku = Buku("Barbie", penulis)

# Akses data penulis dari objek buku
print(buku.info())
print("Nama Penulis:", buku.penulis.nama)
