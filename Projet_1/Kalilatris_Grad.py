print("Grade Calculator")
a=0
som = 0
Lis_Not = []
N=int(input("Konbyen not egzamen ou vle tape : "))
while(a<N):
    Not=int(input("Mete not egzamen ou yo:"))
    while(Not>100):
        Not=int(input("Re mete not egzamen ou yo, paske yo pa dwe depase 100: "))
    a=a+1
    som = som+Not
    Lis_Not.append(Not)
Mwayen = som/N
print("Not ou yo se :",Lis_Not)

if(Mwayen>=90):
    print("Mwayen ou fe an se: ",Mwayen,"/ A.")
if(Mwayen>=80):
    print("Mwayen ou fe an se: ",Mwayen,"/ B.")
if(Mwayen>=70):
    print("Mwayen ou fe an se: ",Mwayen,"/ C.")
if(Mwayen>=60):
    print("Mwayen ou fe an se: ",Mwayen,"/ D.")
if(Mwayen<60):
    print("Mwayen ou fe an se: ",Mwayen,"/ F.")
