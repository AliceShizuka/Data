harga_produk = []
harga_setelah_diskon = []

while True:
    jumlah_produk = len(harga_produk) + 1
    harga = input(f"Masukkan harga produk {jumlah_produk} (atau masukkan '0' untuk selesai): ")
    try:
        harga = float(harga)
        if harga == 0:
            break
        harga_produk.append(harga)

        if harga > 50000:
            harga_diskon = harga * 0.95
            print(f"Produk {jumlah_produk} dapat diskon 5%: Rp {harga_diskon:,.0f}")
        else:
            harga_diskon = harga

        harga_setelah_diskon.append(harga_diskon)
    except ValueError:
        print("Masukkan angka yang valid.")

total_setelah_diskon = sum(harga_setelah_diskon)

total_akhir = total_setelah_diskon * 1.10

print(f"\nTotal setelah pajak dan diskon adalah Rp {total_akhir:,.0f}")
