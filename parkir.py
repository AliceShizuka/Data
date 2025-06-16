def biaya_parkir(jam):
    if jam <= 1:
        return 5000
    elif jam <= 3:
        return 5000 + ((jam - 1) * 4000)
    else:
        return 5000 + 8000 + ((jam - 3) * 3000)

waktu_parkir = float(input("Masukkan lama parkir (dalam jam): "))

if waktu_parkir < 0:
    print("Lama parkir tidak boleh negatif.")
    exit(1)

jam = int(waktu_parkir)
if waktu_parkir != int(waktu_parkir):
    jam += 1

print(f"Biaya parkir: Rp {biaya_parkir(jam):,}")