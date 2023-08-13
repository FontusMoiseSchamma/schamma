'''import re
x=input("Antre on fraz\n")
y=[]
for i in x:
    dijitt=re.findall(r'\d+', x)
    dijitt=[int(dijit) for dijit in dijitt]

print("dijit yo se :")
for i in dijitt:
    print(i)
nb_val=len(dijitt)
print("kantite dijit yo se :" + str(nb_val))... pa bon*'''

a=0
tab=[]
vale1 = input("entre yon karakte: ")
for b in vale1:
    if b.isdigit():
        a=a+1
        tab.append(b)
print("dijit ou yo se :",tab)
print("Men kantite dijit ki nan fraz ou a :",a)
        



'''def retire_espas(Fraz):
    Fraz_modifye = ''.join(Fraz.split())
    return Fraz_modifye

Fraz= "Mwen byen kontan patisipe nan Coding Challenge lan ak Code9Class."

Fraz_modifye = retire_espas(Fraz)
print(Fraz_modifye)'''

'''Fraz = input("Tape fraz ou a: ")

lis = Fraz.split()

for a in lis:
    print(a, end="")'''

'''non=input("Mete nonw :")
lis=non.split()
for a in lis:
    print(a.capitalize(),end=" ")'''


