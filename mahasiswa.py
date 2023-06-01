# Program Alur Pendaftaran Mahasiswa

# Tipe data yang digunakan:
# - String (str): Untuk menyimpan data nama, alamat, dan program studi.
# - Integer (int): Untuk menyimpan data tahun kelahiran dan tahun masuk.
# - Float (float): Untuk menyimpan data nilai rata-rata.

# Meminta input pengguna untuk memulai proses pendaftaran
start = input("Apakah Anda ingin mendaftar sebagai mahasiswa baru? (y/n): ")

if start.lower() == "y":
    print("Silakan masukkan data pendaftaran:")

    # Meminta input pengguna untuk data pribadi
    nama = input("Nama lengkap: ")
    tahun_lahir = int(input("Tahun kelahiran: "))
    alamat = input("Alamat: ")

    # Meminta input pengguna untuk data akademik
    program_studi = input("Program studi yang diminati: ")
    tahun_masuk = int(input("Tahun masuk: "))
    nilai_rata_rata = float(input("Nilai rata-rata: "))

    # Menampilkan data yang telah dimasukkan
    print("\nTerima kasih, berikut adalah data pendaftaran Anda:")
    print("Nama:", nama)
    print("Tahun kelahiran:", tahun_lahir)
    print("Alamat:", alamat)
    print("Program studi yang diminati:", program_studi)
    print("Tahun masuk:", tahun_masuk)
    print("Nilai rata-rata:", nilai_rata_rata)

    # Meminta konfirmasi pembayaran
    pembayaran = input("\nApakah Anda sudah melakukan pembayaran? (y/n): ")

    if pembayaran.lower() == "y":
        print("Pendaftaran berhasil! Selamat bergabung di universitas kami.")
    else:
        print("Silakan selesaikan pembayaran untuk menyelesaikan pendaftaran.")

else:
    print("Terima kasih. Sampai jumpa lain waktu!")
