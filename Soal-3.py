#dimisalkan 
#nilai ujian teori = a
#nilai ujian praktek = b

a = float(input("Masukkan nilai ujian teori: "))
b = float(input("Masukkan nilai ujian praktek: "))

if a >= 70 and b >= 70:
    print("Selamat, Anda lulus")
elif a >= 70 and b < 70:
    print("Anda harus mengulang ujian praktek")
     #dasarnya dari if dan else, kalau ada elif maka dia lebih dari satu 
elif a < 70 and b >= 70:
    print("Anda harus mengulang ujian teori")
else:
     print("Anda harus mengulang ujian teori dan praktek")