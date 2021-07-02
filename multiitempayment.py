tambah="y"
while tambah=="y":
        
    print("")
    print("========================================")
    print(" DAFTAR MENU ")
    print("========================================")
    print(" Menu Makanan ")
    print("========================================")
    print(" 1 = NASI GORENG         Rp 15.000")
    print(" 2 = LONTONG GORENG      Rp 14.900")
    print(" 3 = BAKSO GORENG        Rp 12.900")
    print(" 4 = RUJAK GORENG        Rp 13.000")
    print(" 5 = RUJAK BAKSO         Rp 15.000")
    print(" 6 = RUJAK BAKSO PECEL   Rp 17.000")
    print("========================================")
    print(" Menu Minuman ")
    print("========================================")
    print(" a = TEH DINGIN/PANAS   Rp 2.500")
    print(" b = KOPI DINGIN        Rp 5.000")
    print(" c = KOPI PANAS         Rp 6.500")
    print(" d = COCA COLA DINGIN   Rp 3.500")
    print(" e = COCA COLA DINGIN   Rp 5.000")
    print("========================================")
    print("")

    kodemakanan =['1','2','3','4','5','6']
    namamakanan = ['NASI GORENG','LONTONG GORENG', 'BAKSO GORENG','RUJAK GORENG','RUJAK BAKSO','RUJAK BAKSO PECEL']
    hargamakanan = [15000,14900,12900,13000,15000,17000]
    kodeminuman =['a','b','c','d','e']
    namaminuman = ['TEH DINGIN/PANAS','KOPI DINGIN','KOPI PANAS','COCA COLA DINGIN','COCA COLA DINGIN']
    hargaminuman = [2500,5000,6500,3500,5000]

    pilmakanan = input(">> Masukkan Kode makanan  = ")
    qtymakanan = input(">> Jumlah Makanan         = ")
    pilminuman = input(">> Masukkan Kode minuman  = ")
    qtyminuman = input(">> Jumlah Minuman         = ")
    
    i = 0
    while i<len (namamakanan) and i<len (namaminuman):
        if kodema[i] == pilma and kodemi[i] == pilmi:
            namamak = namamakanan[i] 
            namamin = namaminuman[i]
            hrgsatma = hargamakanan[i] 
            hrgsatmi = hargaminuman[i]
        i+=1
        
        tot_mak = hrgsatma * int(qtymakanan) 
        tot_min = hrgsatmi * int(qtyminuman) 
        tot_byr = tot_mak + tot_min
    
    print(("----------------------------------------"))
    print(">>> NAMA MAKANAN      : " + namamak)
    print(">>> JUMLAH            : " + qtyma)
    print(">>> HARGA MAKANAN     : Rp " + str(tot_mak))
    print(">>> NAMA MINUMAN      : " + namamin)
    print(">>> JUMLAH            : "+ qtymi)
    print(">>> HARGA MINUMAN     : Rp "+ str(tot_min))
    print(("----------------------------------------"))
    print(">>> TOTAL BAYAR       : Rp " + str(tot_byr))
    
    bayar= int (input(">>> BAYAR             : Rp "))
    kembalian= bayar - int(tot_byr)
    print(">>> KEMBALIAN         : Rp "+ str(kembalian))
    
    tambah=input("Pesan lagi (y/t)? ")
    if tambah=="t":
        print("Terima Kasih Telah Berbelanja")
        break