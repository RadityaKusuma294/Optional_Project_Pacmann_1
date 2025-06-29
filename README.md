# Projek python - Mesin kasir sederhana


## Latar Belakang
Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain.
Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi membutuhkan Programmer untuk membuatkan fitur-fitur agar bisa sistem kasir self-service di supermarket itu bisa berjalan dengan lancar.


## Tujuan Utama program
Membuat sistem kasir sederhana yang memungkinkan pelanggan:
1. Menambahkan item belanja.
2. Mengubah data item (nama, jumlah, atau harga).
3. Menghapus item tertentu.
4. Melihat daftar belanja.
5. Mereset semua belanjaan.
6. Melihat total harga dan mendapatkan diskon otomatis sesuai nominal belanja.


## Requirements teknis:
1. Modular Code :  kode program yang ditulis dengan cara memecah fungsionalitas ke dalam bagian-bagian kecil (modul) yang terpisah dan independen.
2. Clean Code (PEP8).
3. Terdapat dokumentasi docstring di function atau class yang dibuat.
4. Terdapat try, error di branching agar mudah untuk melakukan track error (defense programming).
5. Boleh menggunakan library atau method Python.


## Flowchart
![flowchart_converted (1)](https://github.com/RadityaKusuma294/Optional_Project_Pacmann_1/blob/main/images/flowchart_converted%20(1).jpg?raw=true)
#### Start
Program dimulai.

#### Tampilkan Menu
Program akan menampilkan menu utama yang terdiri dari:
1. Input barang
2. Ganti nama barang
3. Ganti jumlah barang
4. Ganti harga barang
5. Tampilkan dan periksa daftar belanja
6. Hapus barang
7. Reset belanja
8. Total belanja
9. Keluar

#### User Input (Pilihan Menu)
User diminta untuk memasukkan angka pilihan sesuai menu (1-9).

#### Menjalankan menu yang dipilih :
1. Input Barang : Input nama barang, jumlah, harga.
2. Ganti Nama Barang : Input nama lama dan nama baru
3. Ganti Jumlah Barang : Input nama barang dan jumlah baru.
4. Ganti Harga Barang : Input nama barang dan harga baru.
5. Mmeriksa & Tampilkan Daftar Belanja
6. Hapus Barang : Input nama barang yang ingin dihapus.
7. Reset Transaksi
8. Total Belanjaan 
9. Exit : Program selesai dan keluar.

#### Loop ke Awal
Setelah setiap proses (kecuali exit), program akan kembali ke menu utama untuk melanjutkan atau melakukan aksi lain.

#### End
Program berakhir setelah user memilih menu nomor 9 (Exit).


## Penjelasan Function
Objek Transaction memiliki atribut utama list_items, sebuah list yang menyimpan semua item belanja dalam bentuk dictionary (nama, jumlah barang, harga).
Method utama dalam class :
1. add_item: Menambahkan barang ke list_items.
2. update_item_name: Mengubah nama barang.
3. update_item_qty: Mengubah jumlah barang.
4. update_item_price: Mengubah harga barang.
5. delete_item: Menghapus barang berdasarkan nama.
6. reset_transaction: Menghapus seluruh daftar belanja.
7. check_order: Menampilkan tabel belanjaan dan validasi apakah ada data kosong atau salah.
8. total_price: Menghitung total harga seluruh item dan menentukan diskon:
   a. 500.000 → diskon 10%
   b. 300.000 → diskon 8%
   c. 200.000 → diskon 5%
9. Fungsi main() :
   a. Menampilkan menu dan meminta input pengguna.
   b. Setiap pilihan akan memanggil method yang sesuai berdasarkan nomor menu tugas.


## Demonstrasi Code
#### Test 1
Customer ingin menambah dua item baru:
1. Nama item: Ayam Goreng, Qty: 2, Harga: 20000
2. Nama item: Pasta Gigi, Qty: 3, Harga: 15000
![kasir_output_1](https://github.com/RadityaKusuma294/Optional_Project_Pacmann_1/blob/main/images/kasir_output_1.jpg?raw=true)
![kasir_output_2](https://github.com/RadityaKusuma294/Optional_Project_Pacmann_1/blob/main/images/kasir_output_2.jpg?raw=true)
    
#### Test 2
Customer ingin menghapus item Pasta Gigi dari daftar belanjaan
![kasir_output_3](https://github.com/RadityaKusuma294/Optional_Project_Pacmann_1/blob/main/images/kasir_output_3.jpg?raw=true)

#### Test 3
Customer ingin menghapus semua daftar belanjaannya
![kasir_output_4](https://github.com/RadityaKusuma294/Optional_Project_Pacmann_1/blob/main/images/kasir_output_4.jpg?raw=true)

#### Test 4
Customer ingin menghitung total belanjaannya
![kasir_output_5](https://github.com/RadityaKusuma294/Optional_Project_Pacmann_1/blob/main/images/revisi.jpg?raw=true)


## Kesimpulan
Program kasir sederhana ini sudah berhasil dibuat dengan semua fitur yang dibutuhkan, seperti menambah, mengubah, menghapus barang, dan menghitung total belanja dengan diskon. Program dibuat menggunakan class dan fungsi agar lebih rapi dan mudah dipahami.

Selain itu, Setiap fungsi juga diberi penjelasan (docstring) untuk memudahkan dalam pembacaan dan membantu dalam memahami function.

Secara keseluruhan, program ini sudah berjalan dengan baik dan bisa dikembangkan lagi untuk fitur yang lebih lengkap ke depannya.



