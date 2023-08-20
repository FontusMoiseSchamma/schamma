import random

with open("database.txt", "w") as fichier:
    pass
fichier.close()

non = input("Antre non ou: ")
siyati = input("Antre siyati ou: ")

min_karaktè = non, siyati

compt =0
for el in min_karaktè:
    compt = compt+1
    if el == ' ':
        compt = compt-1

def jenere_epsedo(non, siyati):
    epsedo1 = f"{non[0]}{siyati[0]}{(compt)}{len(non.replace(' ', ''))}"
    epsedo2 = f"{non.replace(' ', '').lower().title()}{siyati.replace(' ', '').lower()}"
    min_karaktè = min(non, siyati, key=len)
    epsedo3 = f"{min_karaktè[::-1].upper().title()}{random.randint(100, 1000)}"
    return epsedo1, epsedo2, epsedo3


epsedo1, epsedo2, epsedo3 = jenere_epsedo(non, siyati)

with open("database.txt", "r") as fichier:
    kontni_fichye = fichier.read()
    liste_epsedo = kontni_fichye.split(",")
    
kantite = len(liste_epsedo)

print(f"Bonjou {non} {siyati}, nou rekoni nan sèvis nou an")
print(f"nou deja jenere epsedo pou {kantite} moun deja")

with open("database.txt", "a") as fichier:
    fichier.write(f"{epsedo1},{epsedo2},{epsedo3},")

lis_epsedo = [siyati, non, epsedo1, epsedo2, epsedo3]
print("Men epsedo yo")
print(lis_epsedo)
chwa_non = random.choice([epsedo for epsedo in lis_epsedo if len(epsedo) < 7])
print(f"Non ki pi favorab pou itilize sou rezo sosyal se: {chwa_non}")
