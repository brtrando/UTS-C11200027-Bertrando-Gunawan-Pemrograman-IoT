from statistics import mean, stdev
#Membuat List data
data = []

#Memasukan Jumlah Data (N ditentukan oleh pengguna)
n = int(input("Jumlah Data :"))

#Looping sejumlah N/ Berapa banyak data
for i in range (n) :
    nilai = float(input(f"Masukkan Nilai Data ke {i+1} :"))
    data.append(nilai)

#Menunjukkan Hasilnya
print("Nilai Minimum adalah : ",min(data))
print("Nilai Maksimum adalah : ", max(data))
print("Nilai rata-rata adalah : ",mean(data))
print("Nilai Standar Deviasi adalah : ",stdev(data))