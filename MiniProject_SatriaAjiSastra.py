data_timbangan = []

while True:
    print("  SISTEM PENCATATAN SEDERHANA ADMIN POS TIMBANG SAWIT")
    print("1. Tambah Data Truk Masuk (Timbang Bruto)")
    print("2. Lihat Daftar Rekap Timbangan")
    print("3. Ubah Data & Timbang Keluar (Hitung Netto)")
    print("4. Hapus Data Timbangan")
    print("5. Keluar Program")
    
    pilihan = int(input("Pilih menu (1-5): "))
    
    # 1. Masukin Data
    if pilihan == 1:
        print(" INPUT DATA TRUK MASUK ")
        nama = input("Masukkan Nama Supir: ")
        plat = input("Masukkan Nomor Plat Truk: ")
        bruto = int(input("Masukkan Berat Bruto (Kg): "))
        
        data_timbangan.append((nama, plat, bruto, 0, 0))
        print(" Sukses! Data truk berhasil dicatat ke sistem.")

    # 2. Nampilkan rekap data (Tanpa Tabel)
    elif pilihan == 2:
        print(" REKAP DATA TIMBANGAN TRUK SAWIT ")
        if len(data_timbangan) == 0:
            print(" Belum ada data transaksi timbangan.")
        else:
            i = 0
            while i < len(data_timbangan):
                t = data_timbangan[i]
                print(f"Data ke-{i + 1}")
                print(f"  - Supplier   : {t[0]}")
                print(f"  - Plat Truk  : {t[1]}")
                print(f"  - Bruto (Kg) : {t[2]}")
                print(f"  - Tara (Kg)  : {t[3]}")
                print(f"  - Netto (Kg) : {t[4]}")
                print("-" * 30)
                i = i + 1

    # 3. Mengubah Data & Hitung Netto
    elif pilihan == 3:
        print(" PROSES TIMBANG KELUAR & HITUNG NETTO ")
        if len(data_timbangan) == 0:
            print(" Belum ada data truk yang bisa diproses.")
        else:
            i = 0
            while i < len(data_timbangan):
                t = data_timbangan[i]
                print(f"[{i + 1}] Supplier: {t[0]} | Plat: {t[1]} | Bruto: {t[2]}")
                i = i + 1
                
            nomor = int(input("Pilih nomor data truk yang mau ditimbang keluar: "))
            indeks = nomor - 1
            
            if 0 <= indeks < len(data_timbangan):
                data_lama = data_timbangan[indeks]
                tara = int(input("Masukkan Berat Tara / Kosong Truk (Kg): "))
                bruto_lama = data_lama[2]
                
                netto = bruto_lama - tara
                
                if netto < 0:
                    print(" Error: Berat tara tidak boleh lebih besar dari bruto!")
                else:
                    data_timbangan[indeks] = (data_lama[0], data_lama[1], bruto_lama, tara, netto)
                    print(f"Sukses! Berat Bersih (Netto) sawit adalah: {netto} Kg")
            else:
                print(" Nomor truk tidak valid!")

    # 4. hapus data
    elif pilihan == 4:
        print(" HAPUS DATA TIMBANGAN ")
        if len(data_timbangan) == 0:
            print(" Belum ada data untuk dihapus.")
        else:
            i = 0
            while i < len(data_timbangan):
                t = data_timbangan[i]
                print(f"[{i + 1}] Supplier: {t[0]} | Plat: {t[1]}")
                i = i + 1
                
            nomor = int(input("Pilih nomor data yang ingin dihapus: "))
            indeks = nomor - 1
            
            if 0 <= indeks < len(data_timbangan):
                data_timbangan.pop(indeks)
                print(" Data berhasil dihapus dari sistem.")
            else:
                print(" Nomor data tidak ditemukan!")

    # 5. keluar menu
    elif pilihan == 5:
        print("Program selesai. Terima kasih telah menggunakan sistem pos timbang!")
        break
        
    else:
        print("Pilihan tidak valid! Silakan masukkan angka 1 sampai 5.")