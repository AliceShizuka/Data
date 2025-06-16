from kalkubagus import tambah, kurang, kali, bagi
def main():
    while True:
        print("\nMenu:")
        print("1. Penjumlahan")
        print("2. Perkalian")
        print("3. Pengurangan")
        print("4. Pembagian")
        print("5. Exit")

        choice = input("Pilih operasi (1/2/3/4/5): ")

        if choice == '5':
            print("Keluar dari program.")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Masukkan bilangan pertama: "))
                num2 = float(input("Masukkan bilangan kedua: "))
            except ValueError:
                print("Masukkan bilangan yang valid.")
                continue

            if choice == '1':
                print(f"Hasil penjumlahan: {tambah(num1, num2)}")
            elif choice == '2':
                print(f"Hasil perkalian: {kali(num1, num2)}")
            elif choice == '3':
                print(f"Hasil pengurangan: {kurang(num1, num2)}")
            elif choice == '4':
                print(f"Hasil pembagian: {bagi(num1, num2)}")
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()