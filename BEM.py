# Inisialisasi data BEM
bem = []


# Fungsi untuk menambahkan anggota BEM
def tambah_anggota(nama, nim):
    anggota = {"nama": nama, "nim": nim}
    bem.append(anggota)
    print("Anggota baru telah ditambahkan!")


# Fungsi untuk melihat daftar anggota BEM
def lihat_anggota():
    if len(bem) > 0:
        print("Daftar Anggota BEM:")
        for anggota in bem:
            print("Nama:", anggota["nama"])
            print("NIM:", anggota["nim"])
            print("----------------------")
    else:
        print("Belum ada anggota BEM.")


# Fungsi untuk mengupdate data anggota BEM
def update_anggota(nama, nim, nama_baru, nim_baru):
    for anggota in bem:
        if anggota["nama"] == nama and anggota["nim"] == nim:
            anggota["nama"] = nama_baru
            anggota["nim"] = nim_baru
            print("Data anggota berhasil diupdate!")
            return
    print("Anggota tidak ditemukan.")


# Fungsi untuk menghapus anggota BEM
def hapus_anggota(nama, nim):
    for anggota in bem:
        if anggota["nama"] == nama and anggota["nim"] == nim:
            bem.remove(anggota)
            print("Anggota berhasil dihapus!")
            return
    print("Anggota tidak ditemukan.")


# Program utama
while True:
    print("=== UNIVERSITAS TANGERANG RAYA ===")
    print("1. Tambah Anggota")
    print("2. Lihat Anggota")
    print("3. Update Anggota")
    print("4. Hapus Anggota")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        nama = input("Masukkan nama anggota: ")
        nim = input("Masukkan NIM anggota: ")
        tambah_anggota(nama, nim)
    elif pilihan == "2":
        lihat_anggota()
    elif pilihan == "3":
        nama = input("Masukkan nama anggota yang ingin diupdate: ")
        nim = input("Masukkan NIM anggota yang ingin diupdate: ")
        nama_baru = input("Masukkan nama baru: ")
        nim_baru = input("Masukkan NIM baru: ")
        update_anggota(nama, nim, nama_baru, nim_baru)
    elif pilihan == "4":
        nama = input("Masukkan nama anggota yang ingin dihapus: ")
        nim = input("Masukkan NIM anggota yang ingin dihapus: ")
        hapus_anggota(nama, nim)
    elif pilihan == "0":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
