#program kontak
nama_kontak = ["Fawwaz", "John"]
no_telepon = ["08123456789", "08987654321"]

#program menampilkan kontak yang tersimpan di list kontak
def daftar_kontak(): 
    for i in range(len(nama_kontak)):
        print("Nama: {}".format(nama_kontak[i]))
        print("No Telepon: {}".format(no_telepon[i]))

#program untuk menambahkan kontak
def tambah_kontak():  
    nama_kontak.append(input("Nama: "))
    no_telepon.append(input("No Telepon: "))
    print("Kontak berhasil ditambahkan")

print("Selamat datang!")
while True:
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    menu = int(input("Pilih Menu: "))
    if menu == 1:
        daftar_kontak()
    elif menu == 2:
        tambah_kontak()
    elif menu == 3:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia")