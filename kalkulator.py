def inputt():
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        return a, b
    except ValueError:
        print("Input harus berupa angka")
        return inputt()
    
def penjumlahan():
        a, b = inputt()
        hasilt = a + b
        print(f"Hasil penjumlahan: {a} + {b} = {hasilt}")
        return hasilt
def pengurangan():
        a, b = inputt()
        hasilk = a - b
        print(f"Hasil pengurangan: {a} - {b} = {hasilk}")
        return hasilk
def perkalian():
        a, b = inputt()
        hasilp = a * b
        print(f"Hasil perkalian: {a} * {b} = {hasilp}")
        return hasilp
def pembagian():
    try:
        a, b = inputt()
        hasilb = a / b
        print(f"Hasil pembagian: {a} / {b} = {hasilb}")
        return hasilb
    except ZeroDivisionError:
        print("Pembagian dengan nol tidak diperbolehkan")
        return None


print ("KALKULATOR")
print ("1. Penjumlahan")
print ("2. Pengurangan")
print ("3. Perkalian")
print ("4. Pembagian")
print ("5. EXIT")
choice = input("Pilih operasi (1/2/3/4/5)")

while True:
    if choice == '1':
        penjumlahan()
    elif choice == '2':
        pengurangan()
    elif choice == '3':
        perkalian()
    elif choice == '4':
        pembagian()
    elif choice == '5':
        print("Terima kasih telah menggunakan kalkulator!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    choice = input("Pilih operasi (1/2/3/4/5): ")