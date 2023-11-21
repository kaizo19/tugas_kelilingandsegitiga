import latihan_soal

print("-" * 41)
print("pilih bangun ruang yang akan dipilih")
print("1.lingkaran\n2.segitiga")
print("-" * 41)

pilihan = int(input("\nketik pilih :"))

if pilihan == 1:
    print("hitung luas lingkaran")
    r = int(input("masukn nilai jari-jari: "))
    latihan_soal.lingkaran(r)
elif pilihan == 2:
    print("hitung segitiga")
    a = int(input("masukan nilai alas: "))
    t = int(input("masukan nilai tinggi: "))
    latihan_soal.segitiga(a, t)

print("\nprogram selesai! ") 