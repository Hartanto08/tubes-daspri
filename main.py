##libraries

##libraries
import Utilities as u
import csvparser as c
import os
import argparse

#COMMANDS
import F01_F04 as f
from F13_14 import *
from F9 import *
from F10 import *
from F11 import *
from F15_16 import *
from F12 import *

##argparse
parser = argparse.ArgumentParser(description='Menjalankan program membangun candi')
parser.add_argument('folder',type=str,nargs="?",help='folder yang ingin diload')
args = parser.parse_args()

#algoritma
print ("loading . . .",end="")


if __name__ == '__main__' :
    if args.folder is None   :
    ##jika tidak diberi argumen
        print("Tidak ada nama folder yang diberikan!")
        print("Cara penggunaan : python main.py <nama_folder>")
        exit()
    else :
        loaded_folder = load(args.folder)   ##loaded folder akan menyimpan path file

# I N I T I A L    S T A T E 
dataUser = c.initial_data("user.csv",loaded_folder)
dataCandi = c.initial_data("candi.csv",loaded_folder)
dataBahan = c.initial_data("bahan_bangunan.csv", loaded_folder)



loggedIn = [None, None]




while True:
    command = input(">>> ")

    #F01 - Login
    if command == "login":
        loggedIn = f.logIn(dataUser, loggedIn)
        role = loggedIn[1]
  
        
    
    #F02 - LogOut

    elif command == "logout":
        loggedIn = f.logout(loggedIn)

    #F03 - summonJIn
    
    elif command == "summonjin":
        dataUser = f.summonJin(dataUser)
    
    #F04 - hilangkanJIn

    elif command == "hilangkanjin":
        dataUser = f.hilangkanJin(dataUser)
    

    #F09
    elif command == "laporanjin":
            if role == "bandung_bondowoso":
                laporanjin()
            else:
                print("laporanjin hanya dapat diakses oleh akun Bandung Bondowoso.")
    #F10
    elif command ==  "laporancandi":
            if role == "bandung_bondowoso":
                laporancandi(dataCandi)
            else:
                print("laporancandi hanya dapat diakses oleh akun Bandung Bondowoso.")
    #F11
    elif command == "hancurkancandi":
            if role == "roro_jonggrang":
                HancurkanCandi(dataCandi)
            else:
                print("hancurkancandi hanya dapat diakses oleh akun Roro Jonggrang.")
    #F12
    elif command == "ayamberkokok":
            if role == "roro_jonggrang":
                AyamBerkokok(dataCandi)
            else:
                print("ayamberkokok hanya dapat diakses oleh akun Roro Jonggrang.")
        
    #F14
    elif command == "save" :
        save(dataBahan,dataCandi,dataUser)

    #F15
    elif command =="help":
        help(loggedIn)
    
    #F16
    elif command == "exit":
        exit_program(dataBahan,dataCandi,dataUser)


    ##kalau salah ketik command
    else :
         print("input \"help\" untuk bantuan")
        
        
        
        
    

    
