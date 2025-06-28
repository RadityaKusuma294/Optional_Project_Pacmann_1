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
        Menambahkan barang ke dalam list_items.
        """
        barang = {"nama": nama_item, "jumlah barang": jumlah_barang, "harga": harga_per_item}
        self.list_items.append(barang)
        return self.list_items
    
    def update_item_name (self, nama_lama, nama_baru):
        """
        Mengubah nama barang yang ada di list_items.
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
        Mengubah jumlah atau kuantitas barang yang ada di list_items.
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
        Mengubah harga barang yang ada di list_items.
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
        Menghapus salah satu barang belanjaan berdasarkan nama barang.
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
        Menghapus semua barang belanjaan.
        """
        self.list_items.clear()
        print(self.list_items)
        return "semua belanjaan barang anda telah dihapus."
    
    def check_order (self):

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
        Menghitung total harga dan memberikan diskon sesuai nominal pembelian.
        """
        self.total_belanjaan_user = 0
        # for loop untuk menjumlahkan total harga yang di beli pelanggan
        for total in self.list_items:
            self.total_belanjaan_user += (total["jumlah barang"]*total["harga"])
        
        # branching berguna untuk mengetahui diskon yang diperoleh pealnggan berdasarkan total belanjaannnya
        if self.total_belanjaan_user > 200_000:
            diskon = "5%"
            dicount = int(diskon.replace("%",""))/100
            self.total_harga_dengan_diskon = self.total_belanjaan_user - (self.total_belanjaan_user*dicount)
            return f"Total perbelanjaan anda sebesar Rp. {self.total_belanjaan_user} anda mendapat potongan sebesar {diskon}, sehingga anda hanya perlu membayar Rp. {self.total_harga_dengan_diskon}"
        
        elif self.total_belanjaan_user > 300_000:
            diskon = "8%"
            dicount = int(diskon.replace("%",""))/100
            self.total_harga_dengan_diskon = self.total_belanjaan_user - (self.total_belanjaan_user*dicount)
            return f"Total perbelanjaan anda sebesar Rp. {self.total_belanjaan_user} anda mendapat potongan sebesar {diskon}, sehingga anda hanya perlu membayar Rp. {self.total_harga_dengan_diskon}"
        
        elif self.total_belanjaan_user > 500_000:
            diskon = "10%"
            dicount = int(diskon.replace("%",""))/100
            self.total_harga_dengan_diskon = self.total_belanjaan_user - (self.total_belanjaan_user*dicount)
            return f"Total perbelanjaan anda sebesar Rp. {self.total_belanjaan_user} anda mendapat potongan sebesar {diskon}, sehingga anda hanya perlu membayar Rp. {self.total_harga_dengan_diskon}"
        
        else :
            return f"Total perbelanjaan anda sebesar Rp. {self.total_belanjaan_user}"


# input
    def main (self):
        while True:
            print()
            print()
            print("="*60)
            print("MESIN KASIR SEDERHANA PACMANN")
            print("="*60)
            print("1. Input barang belanjaan")
            print("2. Mengganti nama barang belanjaan")
            print("3. Mengganti jumlah barang belanjaan")
            print("4. Mengganti Harga barang belanjaan")
            print("5. Tampilkan Daftar belanjaan")
            print("6. Menghapus salah satu barang belanjaan" )
            print("7. Reset belanjaan")
            print("8. Total Belanjaan")
            print("9. Exit\n")

            choice = int(input('Masukkan Nomor Tugas : '))

            try:

                if choice == 1:
                    nama_barang = input("Masukkan nama barang yang ingin anda beli: ")
                    jumlah = int(input("Masukkan jumlah barang yang ingin anda beli: "))
                    harga = int(input("Masukkan harga barang yang ingin anda beli: "))
                    self.add_item(nama_barang, jumlah, harga)

                elif choice == 2:
                    nama_lama = input("Nama barang yang ingin di ganti: ")
                    nama_baru = input("Nama barang baru: ")
                    print(self.update_item_name(nama_lama, nama_baru))
                
                elif choice == 3:
                    jumlah_lama = input("Jumlah barang yang ingin di ganti: ")
                    jumlah_baru = input("Jumlah barang baru: ")
                    print(self.update_item_name(jumlah_lama, jumlah_baru))
                
                elif choice == 4:
                    harga_lama = input("Harga barang yang ingin di ganti: ")
                    harga_baru = input("Harga barang baru: ")
                    print(self.update_item_name(harga_lama, harga_baru))
                
                elif choice == 5:
                    print(self.check_order())
                
                elif choice == 6:
                    nama_dihapus = input("nama barang yang ingin dihapus: ")
                    print(self.delete_item(nama_dihapus))
                    print(self.check_order())
                
                elif choice == 7:
                    print(self.reset_transaction())
                    self.check_order()
                
                elif choice == 8:
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
# transct_123 = Transaction()
# transaksi_1 = transct_123.add_item("mobil", 1, 23_000_000)
# transaksi_2 = transct_123.add_item("motor", 3, 13_000_000)
# print(transaksi_2)
# print(transct_123.update_item_price("pakaian", 50_000_000))
# print("========================")
# print(transct_123.check_order())
# print(transct_123.total_price())

