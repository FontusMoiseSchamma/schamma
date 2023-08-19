from products import pwodwi_lis, afiche_pwodwi
from cart import ajoute_nan_panye, kalkile_pri_total, panye

def meni():
    print("Byenvini nan boutik la! \n")
    print("1. Chache Pwodwi.")
    print("2. We Panye ak Pri Total.")
    print("3. Femen")

while True:
    meni()
    try:
        chwa = int(input("Chwazi nimero opsyon ou vle a: "))
        if chwa == 1:
            afiche_pwodwi(pwodwi_lis)
            ajoute_nan_panye(pwodwi_lis,panye)
        if chwa == 2:
            print("Men tout pwodwi ki nan panye a:\n")
            a=0
            for b in panye:
                a=a+1
                print(a,b,kalkile_pri_total)
        if chwa == 3:
            print('Boutik la femen')
            break
    except ValueError:
        print('chwa ou a pa nan meni an!')        
   
