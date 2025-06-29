""" 
Program ini berisi daftar tugas dari
sistem kasir sederhana.
    
Anda dapat menjalankan module ini setelah 
dean hanya perlu memasukkan angka pada menu agar program dapat menjalankan
"""

from tabulate import tabulate

class Transaction :
    def __init__(self):
        """
        Inisialisasi objek Transaction dengan list kosong untuk menyimpan item belanja.

        """
        self.list_items = []

    def add_item(self, nama_item, jumlah_barang, harga_per_item):
        """
        Function yang bertujuan untuk menambahkan barang ke dalam list_items (daftar belanjaan).

        Parameter
        ---------
        nama_item (str) = nama barang/produk yang ingin dimasukkan ke daftar belanjaan
        jumlah_barang (int) = jumlah/kuantitas barang yang dibeli
        harga_per_item (int) = Harga barang yang dibeli
        """
        barang = {"nama": nama_item, "jumlah barang": jumlah_barang, "harga": harga_per_item}
        self.list_items.append(barang)
        return self.list_items
    
    def update_item_name (self, nama_lama, nama_baru):
        """
        Function yang bertujuan untuk mengubah nama barang yang ada di list_items (daftar belanjaan).

        Parameter
        ----------
        nama_lama (str) = nama yang ingin dirubah
        nama_baru (str) = nama baru
        """
        try:
        # try-except untuk memeriksa apakah yang nama barang terdapat di dafter belanjaan 
            for i in range(len(self.list_items)):
                if nama_lama in self.list_items[i]["nama"]:
                    self.list_items[i]["nama"] = nama_baru
                    print(self.list_items)
                    return f"{nama_lama} telah diganti dengan {nama_baru}."
                else:
                    raise ValueError ("nama barang anda tidak tersedia.")
        except ValueError as e:
            return e
        
    def update_item_qty (self, nama_item, jumlah_baru):
        """
        Function yang bertujuan untuk mengubah jumlah atau kuantitas barang yang ada di list_items (daftar belanjaan).

        Parameter
        ----------
        nama_item (str) = nama barang yang jumlah/kuantitasnya ingin dirubah
        jumlah_baru (int) = jumlah/kuantitas baru
        """
        try :
        # try-except untuk memeriksa apakah yang nama barang terdapat di dafter belanjaan 
            for i in range(len(self.list_items)):
                if nama_item in self.list_items[i]["nama"]:
                    self.list_items[i]["jumlah barang"] = jumlah_baru
                    print(self.list_items)
                    return f"jumlah produk {nama_item} telah diganti menjadi {jumlah_baru}."
                
            raise ValueError ("nama barang anda tidak tersedia.")
        except ValueError as e:
            return e
        
    
    def update_item_price (self, nama_item, harga_baru):
        """
        Function yang bertujuan untuk Mengubah harga barang yang ada di list_items (daftar belanjaan).

        Parameter
        ----------
        nama_item (str) = nama barang yang harganya ingin dirubah
        harga_baru (int) = harga baru
        """
        try :
        # try-except untuk memeriksa apakah yang nama barang terdapat di dafter belanjaan
            for i in range(len(self.list_items)):
                if nama_item in self.list_items[i]["nama"]:
                    self.list_items[i]["harga"] = harga_baru
                    print(self.list_items)
                    return f"harga produk {nama_item} telah diganti menjadi {harga_baru}."
                
            raise ValueError ("nama barang anda tidak tersedia.")
        except ValueError as e:
            return e
    
    def delete_item (self, nama_item):
        """
        Function yang bertujuan untuk menghapus salah satu barang belanjaan dari list_items (daftar belanjaan) berdasarkan nama barang.

        Parameter
        ----------
        nama_item (str) = nama barang yang ingin dihapus
        """
        try: 
        # try-except untuk memeriksa apakah yang nama barang terdapat di dafter belanjaan 
            for i in range(len(self.list_items)): # for loop untuk menghapus barang berdasarkan index
                if nama_item in self.list_items[i]["nama"]:
                    self.list_items.pop(i)
                    print(self.list_items)
                    return f"item {nama_item} telah terhapus"
                
            raise ValueError ("nama barang anda tidak tersedia.")
        except ValueError as e:
            return e
    
    def reset_transaction (self):
        """
        Function yang bertujuan untuk menghapus semua barang belanjaan dari list_items (daftar belanjaan).

        """
        self.list_items.clear()
        print(self.list_items)
        return "semua belanjaan barang anda telah dihapus."
    
    def check_order (self):
        """
        Function yang bertujuan untuk menampilkan semua list_items (daftar belanjaan) dan untuk memeriksa apakah nama barang belanjaan kosong atau kuantitas barang dan harga berilai 0.
        
        """
        try: 
        # try - except ini bertujuan untuk memeriksa apabila ada belanjaan yang berjumlah 0 dan harganya 0
            for check in self.list_items:
                if check["nama"]=="" or check["jumlah barang"]==0 or check["harga"]==0:
                    raise ValueError 
        except ValueError :
            data_belajaan= []
            for i in range(len(self.list_items)):
                new_dict = {"no": i+1, "Nama Item": self.list_items[i]["nama"], "Jumlah Item": self.list_items[i]["jumlah barang"], "Harga/Item": self.list_items[i]["harga"], "Total Harga": self.list_items[i]["harga"]*self.list_items[i]["jumlah barang"]}
                data_belajaan.append(new_dict)
            
            print (tabulate(data_belajaan, headers = "keys"))
            return "terdapat kesalahan format input"
        else :
        # apabila tidak tertangkap try-catch maka belanjaan sudah benar
            data_belajaan= []
            for i in range(len(self.list_items)):
                new_dict = {"no": i+1, "Nama Item": self.list_items[i]["nama"], "Jumlah Item": self.list_items[i]["jumlah barang"], "Harga/Item": self.list_items[i]["harga"], "Total Harga": self.list_items[i]["harga"]*self.list_items[i]["jumlah barang"]}
                data_belajaan.append(new_dict)
            
            print (tabulate(data_belajaan, headers = "keys"))
            return "Pemesanan sudah benar"


    def total_price(self):
        """
        Function yang bertujuan untuk menghitung total harga dan memberikan diskon sesuai nominal pembelian.

        """
        self.total_belanjaan_user = 0
        # for loop untuk menjumlahkan total harga yang di beli pelanggan
        for total in self.list_items:
            self.total_belanjaan_user += (total["jumlah barang"]*total["harga"])
        
        # branching berguna untuk mengetahui diskon yang diperoleh pealnggan berdasarkan total belanjaannnya
        if self.total_belanjaan_user > 500_000:
            diskon = "10%"
            dicount = int(diskon.replace("%",""))/100
            self.total_harga_dengan_diskon = self.total_belanjaan_user - (self.total_belanjaan_user*dicount)
            return f"Total perbelanjaan anda sebesar Rp. {self.total_belanjaan_user} anda mendapat potongan sebesar {diskon}, sehingga anda hanya perlu membayar Rp. {self.total_harga_dengan_diskon}"
        
        elif self.total_belanjaan_user > 300_000:
            diskon = "8%"
            dicount = int(diskon.replace("%",""))/100
            self.total_harga_dengan_diskon = self.total_belanjaan_user - (self.total_belanjaan_user*dicount)
            return f"Total perbelanjaan anda sebesar Rp. {self.total_belanjaan_user} anda mendapat potongan sebesar {diskon}, sehingga anda hanya perlu membayar Rp. {self.total_harga_dengan_diskon}"

        elif self.total_belanjaan_user > 200_000:
            diskon = "5%"
            dicount = int(diskon.replace("%",""))/100
            self.total_harga_dengan_diskon = self.total_belanjaan_user - (self.total_belanjaan_user*dicount)
            return f"Total perbelanjaan anda sebesar Rp. {self.total_belanjaan_user} anda mendapat potongan sebesar {diskon}, sehingga anda hanya perlu membayar Rp. {self.total_harga_dengan_diskon}"
        
        else :
            return f"Total perbelanjaan anda sebesar Rp. {self.total_belanjaan_user}"


# input
    def main (self):
        """
        Function yang bertujuan untuk memulai suatu program dan menampilkan menu tugas kasir.
        
        """
        while True:
            print()
            print()
            print("="*60)
            print("MENU TUGAS MESIN KASIR SEDERHANA PACMANN")
            print("="*60)
            print("1. Input barang belanjaan")
            print("2. Mengganti nama barang belanjaan")
            print("3. Mengganti jumlah barang belanjaan")
            print("4. Mengganti Harga barang belanjaan")
            print("5. Tampilkan dan periksa daftar belanjaan")
            print("6. Menghapus salah satu barang belanjaan" )
            print("7. Reset belanjaan")
            print("8. Total Belanjaan")
            print("9. Exit\n")

            try:
                choice = int(input('Masukkan Nomor Tugas : '))
            except:
                choice = 0
        
            try:

                if choice == 1:
                    nama_barang = input("Masukkan nama barang yang ingin anda beli: ")
                    jumlah = int(input("Masukkan jumlah barang yang ingin anda beli: "))
                    harga = int(input("Masukkan harga barang yang ingin anda beli: "))
                    self.add_item(nama_barang, jumlah, harga)
                    print()
                    print("==== Barang yang di masukkan ke daftar belanjaan === ")
                    self.check_order()

                elif choice == 2:
                    nama_lama = input("Nama barang yang ingin di ganti: ")
                    nama_baru = input("Nama barang baru: ")
                    print(self.update_item_name(nama_lama, nama_baru))
                
                elif choice == 3:
                    jumlah_lama = input("Nama barang yang jumlahnya ingin di ganti: ")
                    jumlah_baru = input("Jumlah barang baru: ")
                    print(self.update_item_name(jumlah_lama, jumlah_baru))
                
                elif choice == 4:
                    harga_lama = input("Nama barang yang harganya ingin di ganti: ")
                    harga_baru = input("Harga barang baru: ")
                    print(self.update_item_name(harga_lama, harga_baru))
                
                elif choice == 5:
                    print(self.check_order())
                
                elif choice == 6:
                    nama_dihapus = input("Nama barang yang ingin dihapus: ")
                    print(self.delete_item(nama_dihapus))
                    self.check_order()
                
                elif choice == 7:
                    print(self.reset_transaction())
                    self.check_order()
                
                elif choice == 8:
                    self.check_order()
                    print(self.total_price())
                    
                
                elif choice == 9:
                    return "Terima Kasih\n"
                    break

                else:
                    raise ValueError ("input anda salah")
            
            except ValueError as e:
                print (e)
            continue

if __name__ == "__main__":
    transaksi = Transaction()
    print(transaksi.main())


