from Utilities import *
def laporancandi (data_candi):
    
    
    totalCandi=0
    TotalPasir=0
    TotalBatu=0
    TotalAir=0
    harga_total=[]
    for i in range (1,101):
        if data_candi[i]!=None:
            totalCandi+=1
            TotalPasir+=int(data_candi[i][2])
            TotalBatu+=int(data_candi[i][3])
            TotalAir+=int(data_candi[i][4])
            harga_total.attach([[i],[int(data_candi[i][2])*10000 +int(data_candi[i][3])*15000 +int(data_candi[i][4])*7500]])
    for i in range(my_length(harga_total)):
        for j in range(0, my_length(harga_total) - i - 1):
            if harga_total[j] > harga_total[j + 1]:
                harga_total[j],harga_total[j+1]=harga_total[j+1],harga_total[j]
    print(harga_total)
    print(f"> Total Candi: {totalCandi}")
    print(f"> Total Pasir yang digunakan: {TotalPasir}")
    print(f"> Total Batu yang digunakan: {TotalBatu}")
    print(f"> Total Air yang digunakan: {TotalAir}")
    print(f"ID Candi termahal: {harga_total[0][0]}")
    for i in range(my_length(harga_total)):
        for j in range(0, my_length(harga_total) - i - 1):
            if harga_total[j] < harga_total[j + 1]:
                harga_total[j],harga_total[j+1]=harga_total[j+1],harga_total[j]
    print(f"ID Candi termurah: {harga_total[0][0]}")
#laporancandi()