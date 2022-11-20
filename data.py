from prettytable import PrettyTable
x = PrettyTable()

print("Program Input Data Mahasiswa")
print()
tabelNama = PrettyTable(["No" ,"Nama" ,"NIM" ,"Nilai Tugas" ,"Nilai UTS" ,"Nilai UAS" ,"Nilai Akhir"])
a = 0
while True:
    a += 1
    b = input("Masukkan Nama : ")
    c = input("Masukkan NIM : ")
    d = int(input("Masukkan Nilai Tugas : "))
    e = int(input("Masukkan Nilai UTS : "))
    f = int(input("Masukkan Nilai UAS :"))
    g = "{:.2f}".format((d * .30) + (e * .35) + (f * .35))
    tabelNama.add_row([a, b, c, d, e, f, g])
    tabelNama.horizontal_char = "="
    tabelNama.junction_char = "="
    n = input("Tambahkan Data? y/t : ")
    if n == "T" or n == "t":
        break
print(tabelNama)
input("Sekian dan Terimakasih sudah menggunakan program ini...")