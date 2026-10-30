print("--- PILIHAN MENU ---")
print("1. Menghitung Keliling Lingkaran ")
print("2. Menghitung Luas Lingkaran")

pilihan = int(input("Masukkan pilihan angka (1 atau 2): "))
r = float(input("masukkan nilai untik jari-jari: "))

if pilihan == 1:
    keliling = 2 * 3.14 * r
    print("Keliling Lingkaran adalah:", keliling)
elif pilihan ==2:
    luas = 3.14 * r * r
    print("Luas Lingkaran adalah", luas)
else:
    print("pilihan salah! Harap masukkan angka 1 atau 2.")