from tabulate import tabulate

class Transaction :
    def __init__(self):
        self.list_items = []
        pass

    def add_item(self, nama_item, jumlah_barang, harga_per_item):
        barang = {"nama": nama_item, "jumlah barang": jumlah_barang, "harga": harga_per_item}
        self.list_items.append(barang)
        return self.list_items
    
    def update_item_name (self, nama_lama, nama_baru):
        for i in range(len(self.list_items)):
            if nama_lama in self.list_items[i]["nama"]:
                self.list_items[i]["nama"] = nama_baru
                print(self.list_items)
                return f"{nama_lama} telah diganti dengan {nama_baru}."
            continue
        return "nama barang anda tidak tersedia."
    
    def update_item_qty (self, nama_item, jumlah_baru):
        for i in range(len(self.list_items)):
            if nama_item in self.list_items[i]["nama"]:
                self.list_items[i]["jumlah barang"] = jumlah_baru
                print(self.list_items)
                return f"jumlah produk {nama_item} telah diganti menjadi {jumlah_baru}."
            continue
        return "nama barang anda tidak tersedia."
    
    def update_item_price (self, nama_item, harga_baru):
        for i in range(len(self.list_items)):
            if nama_item in self.list_items[i]["nama"]:
                self.list_items[i]["harga"] = harga_baru
                print(self.list_items)
                return f"harga produk {nama_item} telah diganti menjadi {harga_baru}."
            continue
        return "nama barang anda tidak tersedia."
    
    def delete_item (self, nama_item):
        for i in range(len(self.list_items)):
            if nama_item in self.list_items[i]["nama"]:
                self.list_items.pop(i)
                print(self.list_items)
                return f"item {nama_item} telah terhapus"
        return "nama barang anda tidak tersedia."
    
    def reset_transaction (self):
        self.list_items.clear()
        print(self.list_items)
        return "semua belanjaan barang anda telah dihapus."
    
    def check_order (self):
        try: # ini bisa di lihat di pre-class pacmann
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
            data_belajaan= []
            for i in range(len(self.list_items)):
                new_dict = {"no": i+1, "Nama Item": self.list_items[i]["nama"], "Jumlah Item": self.list_items[i]["jumlah barang"], "Harga/Item": self.list_items[i]["harga"], "Total Harga": self.list_items[i]["harga"]*self.list_items[i]["jumlah barang"]}
                data_belajaan.append(new_dict)
            
            print (tabulate(data_belajaan, headers = "keys"))
            return "Pemesanan sudah benar"


    def total_price(self):
        self.total_belanjaan_user = 0
        for total in self.list_items:
            self.total_belanjaan_user += (total["jumlah barang"]*total["harga"])
        
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
transct_123 = Transaction()
transaksi_1 = transct_123.add_item("mobil", 1, 23_000_000)
transaksi_2 = transct_123.add_item("motor", 3, 13_000_000)
print(transaksi_2)
print(transct_123.update_item_price("pakaian", 50_000_000))
print("========================")
print(transct_123.check_order())
print(transct_123.total_price())

