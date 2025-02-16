list_barang = [
    {'ID_barang': 1, 'Nama_barang': 'porstex', 'harga_barang': 30000, 'jumlah_barang': 2, 'kategori': 'kamar mandi'},
    {'ID_barang': 2, 'Nama_barang': 'gelas', 'harga_barang': 7000, 'jumlah_barang': 3, 'kategori': 'dapur'},
    {'ID_barang': 3, 'Nama_barang': 'asbak', 'harga_barang': 20000, 'jumlah_barang': 1, 'kategori': 'kamar'}
]

from tabulate import tabulate

def inputString(string):
    while True:
        object = (input(f'{string}')).strip()
        if object.replace(' ', '').isalnum():
            for c in object:
                if c.isalpha():
                    return object
            print('Data tidak valid. Harus mengandung setidaknya satu huruf.')
        else:
            print('Data tidak valid')

def inputAngka(promp):
    while True:
        try:
            angka = int(input(f'{promp}: '))
            if angka < 0:
                print('\nAngka harus bernilai Positif')
            else:
                break
        except:
            print('\nHanya masukan angka bulat')
    return angka

def menu_utama():
    print("Anda memasuki manajemen inventory")
    while True:
        print("""        
            List Menu :
        1. Menampilkan inventory
        2. Menambah inventory
        3. Menghapus inventory
        4. Mengubah inventory
        5. Keluar Program """)
        menuSatu = inputAngka('Masukkan Menu yang ingin dijalankan')
        if menuSatu == 1:
            print("\nKamu memilih menu 1.")
            menampilkan_inventory()
        elif menuSatu == 2:
            print("\nKamu memilih menu 2.")
            menambah_inventory()
        elif menuSatu == 3:
            print("\nKamu memilih menu 3.")
            menghapus_inventory()
        elif menuSatu == 4:
            print("\nKamu memilih menu 4.")
            mengubah_inventory()
        elif menuSatu == 5:
            while True:
                konfirmasi = inputString("Apakah anda ingin keluar dari program (ya/tidak)").lower()
                if konfirmasi in ['ya', 'tidak']:
                    break
                else:
                    print("Pilihan tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            if konfirmasi == 'ya':
                print("Anda memilih keluar dari program. Terimakasih")
                exit()
            else:
                continue
        else:
            print("\nMenu tidak tersedia, silahkan masukan angka 1 sampai 5")

def menampilkan_inventory():
    if not list_barang: # jika data kosong
        print("\nData kosong!!!. Kembali ke menu utama.")
        menu_utama()
        return
    while True:
        print("""\nMenampilkan inventory :
        1. Tampilkan seluruh inventory
        2. Pilih barang
        3. Kembali ke main menu
        4. Keluar Program""")
        menuSatu = inputAngka('Masukkan Menu yang ingin dijalankan')
        if menuSatu == 1:
            print("\nKamu memilih menu 1.")
            print(tabulate(list_barang, headers="keys", tablefmt="grid"))
        elif menuSatu == 2:
            barangTersedia = [{'ID_barang': x['ID_barang'], 'Nama_barang': x['Nama_barang']} for x in list_barang]
            print("\nKamu memilih menu 2.")
            print("\nPilih barang yang ingin ditampilkan")
            print(tabulate(barangTersedia, headers='keys', tablefmt="grid"))
            while True:
                barangTerpilih = inputAngka('Masukan Nomor barang')
                pilihanBarang = [x for x in list_barang if x["ID_barang"] == barangTerpilih]
                barangTersedia = [{'ID_barang': x['ID_barang'], 'Nama_barang': x['Nama_barang']} for x in list_barang]
                if pilihanBarang:
                    print("\nBarang yang dipilih:")
                    print(tabulate(pilihanBarang, headers="keys", tablefmt="grid"))
                    break
                else:
                    print("\nBarang tidak ditemukan, barang yang tersedia:")
                    print(tabulate(barangTersedia, headers='keys', tablefmt="grid"))
        elif menuSatu == 3:
            menu_utama()
        elif menuSatu == 4:
            while True:
                konfirmasi = inputString("Apakah anda ingin keluar dari program (ya/tidak)").lower()
                if konfirmasi in ['ya', 'tidak']:
                    break
                else:
                    print("Pilihan tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            if konfirmasi == 'ya':
                print("Keluar dari program. Terimakasih!")
                exit()
            else:
                continue
        else:
            print("\nMenu tidak tersedia, silahkan masukan angka 1 sampai 4")

def menambah_inventory():
    while True:
        print("""\nMenambah Inventory:
        1. Menambah barang
        2. Kembali ke menu utama
        3. Keluar Program""")
        pilihan = inputAngka("Masukkan pilihan")
        if pilihan == 1:
            print(tabulate(list_barang, headers="keys", tablefmt="grid"))
            while True:
                nomor_barang = inputAngka("Masukkan ID barang baru")
                barangAda = False  # Check barang sudah ada atau belum
                for x in list_barang:
                    if x['ID_barang'] == nomor_barang:
                        barangAda = True
                        break
                if barangAda:
                    print("\nNomor Barang sudah ada dalam daftar")
                else:
                    break
            while True:
                Nama_barang = inputString("Masukkan nama barang: ")
                namaAda = False
                for x in list_barang:
                    if x['Nama_barang'].lower() == Nama_barang.lower():
                        namaAda = True
                        break
                if namaAda:
                    print("\nNama Barang sudah ada dalam daftar. Silakan masukkan nama barang yang berbeda.")
                else:
                    break
            harga_barang = inputAngka("Masukkan Harga Barang")
            jumlah_barang = inputAngka("Masukkan Jumlah Barang")
            kategori = inputString("Masukkan Kategori Barang: ")
            new_item = {
                'ID_barang': nomor_barang,
                'Nama_barang': Nama_barang,
                'harga_barang': harga_barang,
                'jumlah_barang': jumlah_barang,
                'kategori': kategori
            }
            print("\nBarang yang akan ditambahkan:")
            print(tabulate([new_item], headers="keys", tablefmt="grid"))
            while True:
                konfirmasi = inputString("Apakah anda ingin menambahkan barang ini ke daftar? (ya/tidak)").lower()
                if konfirmasi in ['ya', 'tidak']:
                    break
                else:
                    print("Pilihan tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            if konfirmasi == 'ya':
                list_barang.append(new_item)
                print("\nBarang berhasil ditambahkan!")
                print(tabulate(list_barang, headers="keys", tablefmt="grid"))
            else:
                print("\nBarang tidak ditambahkan.")
            while True:
                lanjut = inputString("Apakah anda ingin menambah barang lagi? (ya/tidak)").lower()
                if lanjut in ['ya', 'tidak']:
                    break
                else:
                    print("Pilihan tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            if lanjut != 'ya':
                break
        elif pilihan == 2:
            menu_utama()
            break
        elif pilihan == 3:
            while True:
                konfirmasi = inputString("Apakah anda ingin keluar dari program (ya/tidak)").lower()
                if konfirmasi in ['ya', 'tidak']:
                    break
                else:
                    print("Pilihan tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            if konfirmasi == 'ya':
                print("Keluar dari program. Terimakasih!")
                exit()
            else:
                continue
        else:
            print("\nPilihan tidak valid. Silakan masukkan angka 1 sampai 3.")

def menghapus_inventory():
    global list_barang
    if not list_barang:
        print("\nData kosong!!!. Kembali ke menu utama.")
        menu_utama()
        return
    while True:
        print("""\nMenghapus Inventory:
        1. Hapus barang
        2. Kembali ke menu utama
        3. Keluar Program""")
        pilihan = inputAngka("Masukkan pilihan")
        if pilihan == 1:
            print(tabulate(list_barang, headers="keys", tablefmt="grid"))
            while True:
                nomor_barang = inputAngka("Masukkan ID barang yang ingin dihapus")
                barangAda = False
                for x in list_barang:
                    if x['ID_barang'] == nomor_barang:
                        barangAda = True
                        break
                if not barangAda:
                    print("\nID Barang tidak ditemukan dalam daftar")
                else:
                    break
            while True:
                konfirmasi = inputString(f"Apakah Anda yakin ingin menghapus barang dengan ID barang {nomor_barang}? (ya/tidak)").lower()
                if konfirmasi in ['ya', 'tidak']:
                    break
                else:
                    print("Pilihan tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            if konfirmasi == 'ya':
                list_barang = [x for x in list_barang if x['ID_barang'] != nomor_barang]
                print("\nBarang berhasil dihapus!")
                print(tabulate(list_barang, headers="keys", tablefmt="grid"))
            else:
                print("\nBarang tidak dihapus.")
            while True:
                if not list_barang:
                    print("\nData kosong!!!. Kembali ke menu utama.")
                    menu_utama()
                    return
                lanjut = inputString("Apakah Anda ingin menghapus barang lagi? (ya/tidak)").lower()
                if lanjut in ['ya', 'tidak']:
                    break
                else:
                    print("Pilihan tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            if lanjut != 'ya':
                break
        elif pilihan == 2:
            menu_utama()
            break
        elif pilihan == 3:
            while True:
                konfirmasi = inputString("Apakah anda ingin keluar dari program (ya/tidak)").lower()
                if konfirmasi in ['ya', 'tidak']:
                    break
                else:
                    print("Pilihan tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            if konfirmasi == 'ya':
                print("Keluar dari program. Terimakasih!")
                exit()
            else:
                continue
        else:
            print("\nPilihan tidak valid. Silakan masukkan angka 1 sampai 3.")

def mengubah_inventory():
    global list_barang
    if not list_barang:
        print("\nData kosong!!!. Kembali ke menu utama.")
        menu_utama()
        return
    while True:
        print("""\nMengubah Inventory:
        1. Ubah barang
        2. Kembali ke menu utama
        3. Keluar Program""")
        pilihan = inputAngka("Masukkan pilihan")
        if pilihan == 1:
            print(tabulate(list_barang, headers="keys", tablefmt="grid"))
            while True:
                nomor_barang = inputAngka("Masukkan ID barang yang ingin diubah")
                barangAda = False
                for x in list_barang:
                    if x['ID_barang'] == nomor_barang:
                        barangAda = True
                        break
                if not barangAda:
                    print("\nID Barang tidak ditemukan dalam daftar")
                else:
                    break
            while True:
                konfirmasi = inputString(f"Apakah Anda yakin ingin mengubah barang dengan ID barang {nomor_barang}? (ya/tidak)").lower()
                if konfirmasi in ['ya', 'tidak']:
                    break
                else:
                    print("Pilihan tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            if konfirmasi == 'ya':
                for x in list_barang:
                    if x['ID_barang'] == nomor_barang:
                        print("\nBarang yang akan diubah:")
                        print(tabulate([x], headers="keys", tablefmt="grid"))
                        break
                while True:
                    Nama_barang = inputString("Masukkan nama barang: ")
                    namaAda = False
                    for x in list_barang:
                        if x['Nama_barang'].lower() == Nama_barang.lower() and x['ID_barang'] != nomor_barang:
                            namaAda = True
                            break
                    if namaAda:
                        print("\nNama Barang sudah ada dalam daftar. Silakan masukkan nama barang yang berbeda.")
                    else:
                        break
                harga_barang = inputAngka("Masukkan Harga Barang")
                jumlah_barang = inputAngka("Masukkan Jumlah Barang")
                kategori = inputString("Masukkan Kategori Barang: ")
                new_item = {
                    'ID_barang': nomor_barang,
                    'Nama_barang': Nama_barang,
                    'harga_barang': harga_barang,
                    'jumlah_barang': jumlah_barang,
                    'kategori': kategori
                }
                print("\nBarang yang akan diubah:")
                print(tabulate([new_item], headers="keys", tablefmt="grid"))
                konfirmasi = inputString("Apakah Anda yakin ingin mengubah barang ini? (ya/tidak)").lower()
                if konfirmasi == 'ya':
                    for i, item in enumerate(list_barang):
                        if item['ID_barang'] == nomor_barang:
                            list_barang[i] = new_item
                            print("\nBarang berhasil diubah!")
                            print(tabulate(list_barang, headers="keys", tablefmt="grid"))
                            break
                elif konfirmasi == 'tidak':
                    print("\nBarang tidak diubah.")
                else:
                    print("Pilihan tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            while True:
                lanjut = inputString("Apakah Anda ingin mengubah barang lagi? (ya/tidak)").lower()
                if lanjut in ['ya', 'tidak']:
                    break
                else:
                    print("Pilihan tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            if lanjut != 'ya':
                break
        elif pilihan == 2:
            menu_utama()
            break
        elif pilihan == 3:
            while True:
                konfirmasi = inputString("Apakah anda ingin keluar dari program (ya/tidak)").lower()
                if konfirmasi in ['ya', 'tidak']:
                    break
                else:
                    print("Pilihan tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            if konfirmasi == 'ya':
                print("Keluar dari program. Terimakasih!")
                exit()
            else:
                continue
        else:
            print("\nPilihan tidak valid. Silakan masukkan angka 1 sampai 3.")

menu_utama()