#Pengguna memilih konversi suhu mana yang ingin dipilih (Jenis Konversi Suhu)
pilihan = int(input("==== Konversi Suhu =====\n1.Celcius ke Fahrenheit\n2.Fahrenheit ke Celcius\nTentukan Pilihan Mu : "))
#Keadaan saat pengguna memilih nomor 1 (Celcius ke Farenheit)
if pilihan == 1 :
    #Data yang diinputkan : Nilai awal, Nilai Akhir, dan increment
    nilaiAwal = float(input("Masukkan Nilai Awal Suhu Celcius : "))
    nilaiAkhir = float(input("Masukkan Nilai Akhir Suhu Celcius :"))
    perubahan = float (input("Masukkan Nilai Increment :"))
    #Kondisi yang harus karena increment
    if nilaiAkhir>nilaiAwal :
        #Looping
        while nilaiAwal<=nilaiAkhir :
            #Proses Konversi
            farenheit = 9 * nilaiAwal / 5 + 32
            print(f"Saat Suhu {nilaiAwal}-Celcius adalah :{farenheit} Farenheit")
            #Proses Increment
            nilaiAwal += perubahan
    else :
        print("!!!GAGAL!!!\nAngka awal harus lebih kecil")
#Keadaan saat pengguna memilih nomor 2 (Farenheit ke Celcius)
elif pilihan == 2 :
    #Data yang diinputkan : Nilai awal, Nilai Akhir, dan increment
    nilaiAwal = float(input("Masukkan Nilai Awal Suhu Farenheit : "))
    nilaiAkhir = float(input("Masukkan Nilai Akhir Suhu Farenheit :"))
    perubahan = float (input("Masukkan Nilai Increment :"))
    #Kondisi yang harus karena increment
    if nilaiAkhir>nilaiAwal :
        #Looping
        while nilaiAwal<=nilaiAkhir :
            #Proses Konversi
            celcius = (nilaiAwal-32)*5/9
            print(f"Saat Suhu {nilaiAwal}-Farenheit adalah :{celcius} Celcius")
            #Proses Increment
            nilaiAwal += perubahan
    else :
        print("!!!GAGAL!!!\nAngka awal harus lebih kecil")
else :
    print("Tidak bisa\nPilihan hanya antara 1 atau 2")