import time


print("____________________________________________________________________________________")

print(" ▄▄▄· ▄▄▄▄▄.▄▄ ·  ▄▄▄· ▄ •▄  ▄· ▄▌▄ •▄     ▪  ▄▄▄       ▄▄ •  ▄▄▄· ▄• ▄▌▄ •▄ ▄▄  ")
print("▐█ ▀█ •██  ▐█ ▀. ▐█ ▀█ █▌▄▌▪▐█▪██▌█▌▄▌▪    ██ ▀▄ █·    ▐█ ▀ ▪▐█ ▀█ █▪██▌█▌▄▌▪██▌")
print("▄█▀▀█  ▐█.▪▄▀▀▀█▄▄█▀▀█ ▐▀▀▄·▐█▌▐█▪▐▀▀▄·    ▐█·▐▀▀▄     ▄█ ▀█▄▄█▀▀█ █▌▐█▌▐▀▀▄·▐█·")
print("▐█ ▪▐▌ ▐█▌·▐█▄▪▐█▐█ ▪▐▌▐█.█▌ ▐█▀·.▐█.█▌    ▐█▌▐█•█▌    ▐█▄▪▐█▐█ ▪▐▌▐█▄█▌▐█.█▌.▀")
print(" ▀  ▀  ▀▀▀  ▀▀▀▀  ▀  ▀ ·▀  ▀  ▀ • ·▀  ▀    ▀▀▀.▀  ▀    ·▀▀▀▀  ▀  ▀  ▀▀▀ ·▀  ▀ ▀ ")

print("____________________________________________________________________________________")
print("____________________________________Informacija_______________________________________")
print("Po kiekvienu klausimu yra pateikiami atsakymai, kurie turi savo numerius. Pasirinkite atsakymą ir įrašykite jo numerį.")
print("___________________________________Registracija____________________________________")
Taskai=0
vardas=input("Koks yra jūsų vardas? ")
print ("Sveiki atvyke į 'Atsakyk ir gauk', ", vardas)


print("________________________________________________________________________________")
time.sleep(2)
print("Pirmas klausimas. Kas sukūrė Python programavimo kalbą?")
print('''1.Guido van Rossum
2.Tim Berners-Lee
3.Larry Page''')
pirmas=input("Jūsų atsakymas:    ")
if pirmas=="1":
    print("TEISINGAI, gavote 1 tašką, tęsiame žaidimą.")
    Taskai=Taskai+1
elif pirmas=="2":
    print("Neteisingai, tęsiame.")
elif pirmas=="3":
    print("Neteisingai, tęsiame.")


print("________________________________________________________________________________")
time.sleep(2)
print("Antras klausimas. Kokia yra pati populiariausia vaikų programavimo kalba?")
print('''1. JavaScript
2. Python
3. Scratch''')
antras=input("Jūsų atsakymas:    ")
if antras=="3":
    print("TEISINGAI, gavote 1 tašką, tęsiame žaidimą.")
    Taskai=Taskai+1
elif antras=="1":
    print("Neteisingai, tęsiame.")
elif antras=="2":
    print("Neteisingai, tęsiame.")


print("________________________________________________________________________________")
time.sleep(2)
print("Trečias klausimas. Kas yra masyvas?")
print('''1. Duomenų struktūra
2. Tam tikras failas.''')
trecias=input("Jūsų atsakymas:    ")
if trecias=="1":
    print("TEISINGAI, gavote 1 tašką, tęsiame žaidimą.")
    Taskai=Taskai+1
elif trecias=="2":
    print("Neteisingai, tęsiame.")


print("________________________________________________________________________________")
time.sleep(2)
print("Ketvirtas klausimas. Ar Java ir JavaScript kalbos perėmė C kalbos sintaksę? ")
print('''1. Taip
2. Ne ''')
ketvirtas = input("Jūsų atsakymas:    ")
if ketvirtas == "1":
    print("TEISINGAI, gavote 1 tašką, tęsiame žaidimą.")
    Taskai=Taskai+1
elif ketvirtas == "2":
    print("Neteisingai, tęsiame.")


print("________________________________________________________________________________")
time.sleep(2)
print("Penktas klausimas. Ar Python yra priskiriamas Front-End?")
print('''1. Taip
2. Ne''')
trecias=input("Jūsų atsakymas:    ")
if trecias=="1":
    print("Neteisingai, tęsiame.")
elif trecias=="2":
    print("TEISINGAI, gavote 1 tašką, tęsiame žaidimą.")
    Taskai=Taskai+1



print("________________________________________________________________________________")
time.sleep(2)
print("Šeštas klausimas. Ar ši viktorina jums patiko?")
print('''1.Ne 
2.Taip''')
penktas = input("Jūsų atsakymas: ")


print("________________________________________________________________________________")
print ("Jūs surinkote",Taskai,"taškus.")
if Taskai==5:
    print("Jūs atsakėte į visus klausimus teisingai, sveikinimai!!!")
    
