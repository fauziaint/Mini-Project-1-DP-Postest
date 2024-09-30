print("Data Diri Pembeli Mahasiswa ")

nama=input("Masukkan Nama : ")
nim=input("Masukkan Nim : ")
program_Studi=input("Masukkan Program Studi : ")

print("----------------------------")
print("Harga yang harus dibayar", nama)
print("----------------------------")

while True: 
    jumlah_pembelian=int(input("Masukkan Jumlah Barang : "))
    harga_barang=int(input("Masukkan Harga Barang : "))

    if (harga_barang > 250000):
        harga_diskon = harga_barang - (harga_barang * 25/100)
        print("Harga awal :", harga_barang)
        print("Harga dengan diskon :", harga_diskon)
    else:
        print("Harga Asli :", harga_barang)
        print("Tidak mendapatkan diskon")

    keluar = input("Apakah ingin keluar dari Kasir? (y/x):")
    if keluar == "y":
        print("Terima Kasih Telah Berbelanja", nama)
        break
    