import time
from time import sleep
import os 
from os import system

print("Who does your crush?")
print("* 1.M")
print("* 2.S")
print("* 3.N")
print("* 4.T")
print("* 5.V")
losi = int(input("* Please choose: "))
print("")
sleep(0.5)
print("  Please Wait ...")

sleep(3)
system('cls')
losivn = str(input("* Enter PassWord: "))
if(losi == 1):
    hung = "M"
elif(losi == 2):
    hung = "S"
elif(losi == 3):
    hung = "N"
elif(losi == 4):
    hung = "T"
elif(losi == 5):
    hung = "V"
if(losivn == "<3"):
    print("Password Correct")
    print("")
    sleep(1)
    print("                                                          *  *     *  *")
    sleep(1)
    print("                                                       *        *        *")
    sleep(1)
    print("                                                       *       ",hung,"       *")
    sleep(1)
    print("                                                          *           *")
    sleep(1)
    print("                                                             *     *")
    sleep(1)
    print("                                                                *")
    print("")
    print("")
    sleep(0.1)    
    print("########  ##    ## ##       ##     ## ")
    sleep(0.1) 
    print("##     ##  ##  ##  ##       ###   ### ")
    sleep(0.1) 
    print("##     ##   ####   ##       #### #### ")
    sleep(0.1) 
    print("##     ##    ##    ##       ## ### ## ")
    sleep(0.1) 
    print("##     ##    ##    ##       ##     ## ")
    sleep(0.1) 
    print("##     ##    ##    ##       ##     ## ")
    sleep(0.1) 
    print("########     ##    ######## ##     ## ")
    print("")
    print("")
    print("                                                                                      Source: Nguyễn Thế Mạnh")
    print("                                                                                      Idea: Manh nốt")
    sleep(0.1)
    print("")
else:
    print("Password Incorrect")
