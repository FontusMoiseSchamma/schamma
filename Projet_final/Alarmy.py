import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame
import time

pygame.init()
pygame.mixer.init()

son = None

def alam():
    print("\nAlam! Alam! Alam! Alam! Alam!")
    tan = int(input('antre nan ki kantite tan ou vle aksyon sa fet:'))
    if tan == 0 or tan == 1:
        t = 3
        time.sleep(t)
    else:
        t = tan * 60
        time.sleep(t)
    
    global son
    son_path = 'Alam.wav'  
    if os.path.exists(son_path):
        if son:
            son.stop()
        son = pygame.mixer.Sound(son_path)
        son.play()
        print(f"Son an ap jwe nan {t} segond")
    else:
        print("Pa gen son alam.")

print("     ALARMY\n-----------------")

def main():
    global son
    while True:
        print("\nChwazi yon aksyon:")
        print("F - Femen odinate a.")
        print("R - Redemare odinate a.")
        print("A - Alam.")
        print("K - Kanpe alam nan.")
        print("s - Soti nan pwogram nan.")
        
        choice = input("\nChwazi yon aksyon: (F\ R\ A\ S\ K): ").lower()

        if choice == 'f':
            tan = int(input('Antre apre konbyen minit ou vle odinte a femen:'))
            if tan == 0 or tan == 1:
                t= 59
            else:
                t = tan*60    
            os.system(f"shutdown /s /t {t}")
            print(f"Odinate w la ap femen nan {t} segond.")

        elif choice == 'r':
            tan = int(input('Antre apre konbyen minit ou vle odinate redemare:'))
            if tan == 0 or tan == 1:
                t= 59
            else:
                t = tan*60    
            time.sleep(2)
            os.system("shutdown /r /t {1}")
            print(f"Odinate w la ap redemare nan {t} segond.")
            
        elif choice == 'a': 
            alam()                    

        elif choice == 'k':
            if son:
                son.stop()
            else:
                print("Pa gen alam k'ap jwe.")

        elif choice == 's':
            if son:
                son.stop()
            print("Ou soti nan pwogram nan.")
            break

        else:
            print("Chwa ou fe a pa valab. Tanpri, chwazi yon opsyon ki valab.")

if __name__ == "__main__":
    main()
