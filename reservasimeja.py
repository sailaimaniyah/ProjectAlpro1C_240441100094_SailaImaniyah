# Daftar meja dengan kategori
meja_restoran = [
    {"id": 1, "status": "Tersedia", "nama": None, "tanggal": None, "kategori": "Biasa", "harga": 50000, "harga_awal": 50000},
    {"id": 2, "status": "Tersedia", "nama": None, "tanggal": None, "kategori": "Biasa", "harga": 50000, "harga_awal": 50000},
    {"id": 3, "status": "Tersedia", "nama": None, "tanggal": None, "kategori": "Biasa", "harga": 50000, "harga_awal": 50000},
    {"id": 4, "status": "Tersedia", "nama": None, "tanggal": None, "kategori": "Biasa", "harga": 50000, "harga_awal": 50000},
    {"id": 5, "status": "Tersedia", "nama": None, "tanggal": None, "kategori": "VIP", "harga": 100000, "harga_awal": 100000},
    {"id": 6, "status": "Tersedia", "nama": None, "tanggal": None, "kategori": "VIP", "harga": 100000, "harga_awal": 100000},
    {"id": 7, "status": "Tersedia", "nama": None, "tanggal": None, "kategori": "VIP", "harga": 100000, "harga_awal": 100000},
]

# Diskon member
DISKON_MEMBER = 0.15  # 15% diskon untuk member

# Menampilkan daftar meja berdasarkan kategori
def tampilkan_meja():
    print("Tampilkan Daftar Meja")
    print("1. Semua Meja")
    print("2. Meja VIP")
    print("3. Meja Biasa")
    pilihan_kategori = input("Pilih kategori meja (1/2/3): ")

    if pilihan_kategori == "1":
        meja_terpilih = meja_restoran
    elif pilihan_kategori == "2":
        meja_terpilih = [meja for meja in meja_restoran if meja["kategori"] == "VIP"]
    elif pilihan_kategori == "3":
        meja_terpilih = [meja for meja in meja_restoran if meja["kategori"] == "Biasa"]
    else:
        print("Pilihan tidak valid.")
        return

    print("Daftar Meja:")
    for meja in meja_terpilih:
        tanggal = meja["tanggal"] if meja["tanggal"] else "-"
        nama = meja["nama"] if meja["nama"] else "-"
        print(f"Meja {meja['id']} Kategori: {meja['kategori']}: {meja['status']}, Nama: {nama}, Tanggal: {tanggal}, Harga: Rp{meja['harga']})")

# Reservasi meja dengan diskon member
def reservasi_meja():
    try:
        meja_id = int(input("Masukkan nomor meja yang ingin dipesan: "))
        nama_pemesan = input("Masukkan nama pemesan: ")
        tanggal_reservasi = int(input("Masukkan tanggal reservasi (YYYYMMDD): "))
        is_member = input("Apakah pemesan adalah member? (y/n): ")

        for meja in meja_restoran:
            if meja["id"] == meja_id:
                if meja["status"] == "Tersedia":
                    meja["status"] = "Dipesan"
                    meja["nama"] = nama_pemesan
                    meja["tanggal"] = tanggal_reservasi

                    # Menghitung harga dengan diskon jika member
                    harga_awal = meja["harga_awal"]
                    if is_member == "y":
                        harga_diskon = harga_awal * (1 - DISKON_MEMBER)
                        meja["harga"] = int(harga_diskon)
                        print(f"Member mendapatkan diskon 15%! Harga setelah diskon: Rp{meja['harga']}.")
                    else:
                        meja["harga"] = harga_awal
                        print(f"Harga reservasi meja: Rp{meja['harga']}.")
                    
                    print(f"Meja {meja_id} berhasil dipesan atas nama {nama_pemesan} untuk tanggal {tanggal_reservasi}.")
                else:
                    print(f"Meja {meja_id} sudah dipesan.")
                return
        print("Nomor meja tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Harap masukkan data yang benar.")

# Update reservasi
def update_reservasi():
    try:
        meja_id = int(input("Masukkan nomor meja yang ingin diperbarui: "))
        nama_baru = input("Masukkan nama pemesan baru: ")
        tanggal_reservasi_baru = int(input("Masukkan tanggal reservasi baru (YYYYMMDD): "))

        for meja in meja_restoran:
            if meja["id"] == meja_id:
                if meja["status"] == "Dipesan":
                    meja["nama"] = nama_baru
                    meja["tanggal"] = tanggal_reservasi_baru
                    print(f"Nama pemesan meja {meja_id} berhasil diperbarui menjadi {nama_baru}.")
                else:
                    print(f"Meja {meja_id} belum dipesan, tidak bisa memperbarui nama.")
                return
        print("Nomor meja tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Harap masukkan data yang benar.")

# Batalkan reservasi
def batalkan_reservasi():
    try:
        meja_id = int(input("Masukkan nomor meja yang ingin dibatalkan: "))

        for meja in meja_restoran:
            if meja["id"] == meja_id:
                if meja["status"] == "Dipesan":
                    # Membatalkan reservasi
                    meja["status"] = "Tersedia"
                    meja["nama"] = None
                    meja["tanggal"] = None
                    meja["harga"] = meja["harga_awal"]  # Mengembalikan harga ke harga awal
                    print(f"Reservasi meja {meja_id} berhasil dibatalkan.")
                else:
                    print(f"Meja {meja_id} belum dipesan, tidak ada yang perlu dibatalkan.")
                return
        print(f"Nomor meja {meja_id} tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Harap masukkan nomor meja yang benar.")

# Menu utama
def menu():
    while True:
        print("--- Sistem Reservasi Meja Restoran ---")
        print("1. Tampilkan Daftar Meja")
        print("2. Reservasi Meja")
        print("3. Update Reservasi")
        print("4. Batalkan Reservasi")
        print("5. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5): ")
        if pilihan == "1":
            tampilkan_meja()
        elif pilihan == "2":
            reservasi_meja()
        elif pilihan == "3":
            update_reservasi()
        elif pilihan == "4":
            batalkan_reservasi()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
menu()