def hitungKembalian(harga, dibayar):
    a = dibayar - harga
    kembalian = int(a + harga*10/100 if harga > 200000 else a)
    
    stok = [50000,20000,10000,5000]
    tersedia = []
    kembalian2 = kembalian
    for x in stok:
        a = kembalian2 // x
        kembalian2 -= x*a
        tersedia.append(a)
    print("Kembalian anda adalah : Rp.", kembalian)
    print("opsi kembalian : ")
    terkover = []
    for i in range(len(stok)):
        if tersedia[i]== 0:
            pass
        else:
            print(tersedia[i], "x", stok[i] )
            terkover.append(stok[i])
    sisa = kembalian - sum(terkover)
    print(sisa, " Disumbangkan karena tidak ada pecahan dibawah 5000")
hitungKembalian(220000,250000)