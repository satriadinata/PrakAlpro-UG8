# Joni Menyimpan data pengunjung dan pemberian wisit saat idul fitri
loop=True
while loop==True:
    print('menu\n1. tambah pengunjung\n2. Lihat pengunjung\n3. Keluar')
    select=input('Pilih menu: ')
    if select=='1':
        store=''
        nama=input('Masukkan nama: ')
        hp=input('Masukkan no hp: ')
        store+=nama+'-'+hp+'\n'
        db=open('data.txt','a+')
        db.write(store)
        db.close()
    elif select=='2':
        db=open('data.txt','r')
        no=1
        for line in db:
            pecah=line.split('-')
            print('No\tNama\t\tNo HP')
            print(str(no)+'\t'+pecah[0]+'\t\t'+pecah[1])
            no+=1
        db.close
    elif select=='3':
        loop='False'
    else:
        print('Tidak ada di menu')