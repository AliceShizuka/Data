def total_pembelian(harga_produk):
    total = sum(harga_produk)
    diskon = 0 
    if total > 100000:
        diskon = total * 0.1
    total_akhir = total - diskon
    return {
        'total': total,
        'diskon': diskon,
        'total_akhir': total_akhir
    }
harga_produk = []
while True:
    jumlah_produk = len(harga_produk) + 1
    harga = input(f"Masukkan harga produk {jumlah_produk} (atau masukkan '0' untuk selesai): ")
    try:
        harga = float(harga)
        if harga == 0:
            break
        harga_produk.append(harga)
    except ValueError:
        print("Masukkan harga yang valid.")

hasil = total_pembelian(harga_produk)
print(f"Total sebelum diskon: Rp {hasil['total']}")
print(f"Diskon 10%: Rp {hasil['diskon']}")
print(f"Total setelah diskon: Rp {hasil['total_akhir']}")