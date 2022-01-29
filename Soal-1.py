# Program Kontak
# List Kontak
namakontak = ['Anggi', 'Emeliani']
nomor_tlp = ['089682313699', '081553519536']

# fungsi untuk menampilkan kontak yang tersimpan di list kontak
def daftar_kontak():
    print('Daftar Kontak:')
    for i in range(len(namakontak)):
        print('Nama: {}'.format(namakontak[i]))
        print('No Telepon: {}'.format(nomor_tlp[i]))

# fungsi untuk menambahkan kontak
def tambah_kontak():
    namakontak.append(input('Nama: '))
    nomor_tlp.append(input('No Telepon: '))
    print('Kontak berhasil ditambahkan')


print('Selamat datang!')
while True:
    print('--- Menu ---')
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. Keluar')
    menu = int(input('Pilih Menu: '))
    if menu == 1:
        daftar_kontak()
    elif menu == 2:
        tambah_kontak()
    elif menu == 3:
        print('Program selesai, sampai jumpa!')
        break
    else:
        print('Menu tidak tersedia.')