import os
from sys import platform
from datetime import datetime
import time
d=datetime.now()

if platform == "linux" or platform == "linux2":
    def clear():
        os.system("clear")
else:
    def clear():
        os.system("cls")

aski=r"""
Only for Linux & Windows users


oooooo   oooooo     oooo  o8o  oooo              ooooooooo.                               
 `888.    `888.     .8'   `"'  `888              `888   `Y88.                             
  `888.   .8888.   .8'   oooo   888  oooo    ooo  888   .d88'  .oooo.    .oooo.o  .oooo.o 
   `888  .8'`888. .8'    `888   888   `88.  .8'   888ooo88P'  `P  )88b  d88(  "8 d88(  "8 
    `888.8'  `888.8'      888   888    `88..8'    888          .oP"888  `"Y88b.  `"Y88b.  
     `888'    `888'       888   888     `888'     888         d8(  888  o.  )88b o.  )88b 
      `8'      `8'       o888o o888o     .8'     o888o        `Y888""8o 8""888P' 8""888P' 
                                     .o..P'                                               
                                     `Y8P'                                 By Clud               

"""
print("\033[0;35m",aski,"\033[0;31m")   

test=0
#lists
dico={"a":"@","a":"4","e":"3","i":"1","l":"1","o":"0"}

spicy=['', '!', '@', '/#', '$', '!@', '!@#', '!@#$', '123!', '!123', '1@']+[d.strftime("%A"),d.strftime("%Y")]


mot=(input("KEYWORDS (espace-their by a , ) : ")).lower().split(",")
save=mot[:]
pref=[]

temps=0.001
# Variants creator


long_p=len(pref)
for char in range(long_p):
    for i in range(long_p):
        for j in range(long_p):
            pref.append(pref[char]+pref[i]+pref[j])

#SPICY
long_m=len(mot)


#var change
#fonction
mod_prefix="X"
mod_number="X"
mod_spicy="X"
mod_charge="X"
def table_mod(a,b,c,d):
    print("\033[0;36m")
    print("Mods :")
    print("|")
    print("-- Prefix ["+a+"]")
    print("|")
    print("-- Number ["+b+"]")
    print("|")
    print("-- Strange ["+c+"]")
    print("|")
    print("-- Charge Bar ["+d+"]")
    print("\033[0;31m")


key=mot
long_k=long_m
table_mod(mod_prefix,mod_number,mod_spicy,mod_charge)
print("")
time.sleep(0.5)
if "y" in input("prefix list ? (Y/N) : "):
    print("")
    prefixe=int(input("prefix weight (1,2,3...) : "))
    for elt in range(len(save)):
        for p in range(prefixe):
            if save[elt][:p+1] not in pref:
                pref.append(save[elt][:p+1])
    long_p=len(pref)
    print("")
    prefix_mod=input("prefix mod (light,normal,hard) : ")
    if prefix_mod == "hard":
        for char in range(long_p):
            for i in range(long_p):
                for j in range(long_p):
                    pref.append(pref[char]+pref[i]+pref[j])
    elif prefix_mod == "normal":
        for char in range(long_p):
            for i in range(long_p):
                pref.append(pref[char]+pref[i])
    long_p=len(pref)      
    key+=pref
    long_k+=long_p
    mod_prefix="✔"
clear()
print("\033[0;35m",aski,"\033[0;36m")
table_mod(mod_prefix,mod_number,mod_spicy,mod_charge)
print("")
time.sleep(0.5)
if "y" in input("number list ? (Y/N) : "):
    print("")
    lim_num=int(input("number max : "))
    key+=[str(c) for c in range(lim_num)]
    long_k+=lim_num
    mod_number="✔"
clear()
print("\033[0;35m",aski,"\033[0;36m")
table_mod(mod_prefix,mod_number,mod_spicy,mod_charge)
print("")
time.sleep(0.5)
if "y" in input("strange char ? (Y/N) : "):
    for elt in range(long_m):
        for ltr in range(len(mot[elt])):
            lettre = mot[elt][ltr]
            if lettre in dico:
                special = mot[elt][:ltr] + dico[lettre] + mot[elt][ltr + 1:]
                spicy.append(special)
                temp_variants = []
                for ltr2 in range(len(special)):
                    lettre2 = special[ltr2]
                    temp_variants.append(special[:ltr2] + lettre2.upper() + special[ltr2 + 1:])
                spicy.extend(temp_variants)
            spicy.append(mot[elt][:ltr] + lettre.upper() + mot[elt][ltr + 1:])
    long_s=len(spicy)
    key+=spicy
    long_k+=long_s
    mod_spicy="✔"

clear()
print("\033[0;35m",aski,"\033[0;36m")
table_mod(mod_prefix,mod_number,mod_spicy,mod_charge)
print("")
time.sleep(0.5)
if "y" in input("Show Charge-Bar ? (Y/N) Better performence if this one is disable : "):
    show_chargebar=True
    mod_charge="✔"
else:
    show_chargebar=False

clear()
print("\033[0;35m",aski,"\033[0;36m")
table_mod(mod_prefix,mod_number,mod_spicy,mod_charge)
print("")
time.sleep(1)

long_max=long_k**3

#fonction
def interface(p,n,s):
    return 0

def charge_bar(c,longueur=long_max):
    pourcentage=(c/longueur)*100
    print("["+("#"*int(pourcentage))+("."*int(100-pourcentage))+"] "+(str(int(pourcentage))+"% ( "+str(c)+"/"+str(longueur)+" words )"))
    
    
#code
time_save=int(time.time())
charge=0
l=[]

if show_chargebar:
    if long_max<50000000:
        for char in range(long_k):
            charge+=long_k**2
            clear()
            charge_bar(charge)
            for i in range(long_k):
                for j in range(long_k):
                    l.append(key[char]+key[i]+key[j])
    else: #opti
        for char in range(long_k):
            charge+=long_k**2
            charge_bar(charge)
            for i in range(long_k):
                for j in range(long_k):
                    l.append(key[char]+key[i]+key[j])
else:
    for char in range(long_k):
        for i in range(long_k):
            for j in range(long_k):
                l.append(key[char]+key[i]+key[j])
                
clear()

time_save=time.time()-time_save
words_sec=(long_max//time_save)
words_sec="( "+str(words_sec)+" w.s )"
print("\033[0;35m",aski,"\033[0;36m")
print("")
print("\033[0;33m",str(int(time_save))+"s","\033[0;36m")
print("")
print(save)
print("")
charge_bar(long_max)
print("")
print("\033[0;32m","SUCCESS !!\n","\033[0;36m")

txt_name=input("name of your txt file (The file name must not already exist)  : ")

if platform == "linux" or platform == "linux2":
        with open(txt_name+".txt","w") as fichier:
            for elt in l:
                fichier.write(elt+"\n")
else:
    way=os.path.dirname(os.path.abspath(__file__))
    with open(way+chr(92)+txt_name+".txt","w") as fichier:
        for elt in l:
            fichier.write(elt+"\n")
print("")
print("\033[0;32m","Verify if a word exist in this list !")
print("")
print("(exit) for finish the process \n","\033[0;36m")
a=""
while a !="exit":
    a=input("search word : ")
    print("\033[0;32m",a in l,"\033[0;36m")