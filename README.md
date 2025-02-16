# Manajemen-inventory-penginapan
Capstone project Reza JCDS-0608-BDG

Program ini adalah aplikasi manajemen inventaris yang memungkinkan pengguna untuk menampilkan, menambah, menghapus, dan mengubah data barang dalam _inventory_. 
Program ini menggunakan modul `tabulate` untuk menampilkan data dalam format tabel yang rapi.

## Menu Utama:
pragram ini memiliki 5 menu utama yang terdiri dari

1. **Menampilkan Inventory**:
   - Menampilkan seluruh inventaris.
   - Memilih dan menampilkan barang tertentu.

2. **Menambah Inventory**:
   - Menambah barang baru ke dalam inventaris.
   - Memastikan ID barang dan nama barang unik sebelum menambahkannya.

3. **Menghapus Inventory**:
   - Menghapus barang dari inventaris berdasarkan ID barang.
   - Memastikan barang ada dalam daftar sebelum menghapusnya.

4. **Mengubah Inventory**:
   - Mengubah detail barang yang ada dalam inventaris.
   - Memastikan nama barang yang baru tidak sama dengan barang lain dalam daftar.

5. **Keluar Program**:
   - Mengakhiri program


  
program ini juga terdiri dari 5 _main funtion_ dan 2 _input funtion_, _input funtion_ juga berfungsi sebagai _error handling_ yang bisa terjadi ketika input tidak sesuai

## _main funtion_:
1. **menu_utama()**:
   - Menampilkan menu utama dan menangani pilihan pengguna untuk menampilkan, menambah, menghapus, atau mengubah inventaris, atau keluar dari program.

2. **menampilkan_inventory()**:
   - Menampilkan seluruh inventaris atau barang tertentu berdasarkan pilihan pengguna.

3. **menambah_inventory()**:
   - Menambah barang baru ke dalam inventaris dengan memastikan ID dan nama barang unik.

4. **menghapus_inventory()**:
   - Menghapus barang dari inventaris berdasarkan ID barang dengan memastikan barang ada dalam daftar.

5. **mengubah_inventory()**:
   - Mengubah detail barang yang ada dalam inventaris dengan memastikan nama barang yang baru tidak sama dengan barang lain dalam daftar.

## _input funtion_:
1. **inputString()**:
   - Meminta input dari pengguna berupa huruf atau gabungan huruf angka dan memastikan input mengandung setidaknya satu huruf.

2. **inputAngka()**:
   - Meminta input angka dari pengguna dan memastikan input adalah angka bulat positif.
