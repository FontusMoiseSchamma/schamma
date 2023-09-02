import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame
import time

pygame.init()
pygame.mixer.init()

son = None

def alam():
    try:
        print("\nAlam! Alam! Alam! Alam! Alam!")
        tan = int(input('antre nan ki kantite tan ou vle aksyon sa fet antre l en minute:'))
        if tan == 0 or tan == 1:
            t = 3
            time.sleep(t)
        else:
            t = tan * 60
            time.sleep(t)
        
        global son
        son_path = 'Alam.wav'  # Remplacez 'kirk.mp3' par le chemin complet de votre fichier audio
        if os.path.exists(son_path):
            if son:
                son.stop()
            son = pygame.mixer.Sound(son_path)
            son.play()
        else:
            print("Pa gen son alam. Tanpri, chwazi yon son k ap jwe kòm alam.")
    except pygame.error as e:
        print(e)   
    except ValueError as e:
        print(f"{e} mete tan an chiff")         

print("     ALARMY\n-----------------")

def main():
    global son
    while True:
        print("\nChwazi yon aksyon:")
        print("F - Femen odinate a")
        print("R - Redemare odinate a")
        print("A - Alam")
        print("K - Kanpe son an")
        print("s - Soti nan pwogram nan")
        
        choice = input("\nChwazi yon aksyon: (F\ R\ A\ S\ K): ").lower()

        if choice == 'f':
            try:
                tan = int(input('antre nan ki kantite tan ou vle aksyon sa fet:'))
                if tan == 0 or tan == 1:
                    t= 3
                else:
                    t = tan*60    
                os.system(f"shutdown /s /t {t}")
                print(f"Odinate w la ap femen nan {t} segond.")
            except ValueError as e:
                print(f"{e} ou dwe antre yon chif")    

        elif choice == 'r':
            try:
                tan = int(input('antre nan ki kantite tan ou vle aksyon sa fet:'))
                if tan == 0 or tan == 1:
                    t= 30
                else:
                    t = tan*60    
                time.sleep(2)
                os.system(f"shutdown /r /t {t}")
                print(f"Odinate w la ap redemare nan {t} segond.")
            except ValueError as e:
                print(f"{e} ou dwe antre yon chif") 
            
            
        elif choice == 'a': 
            alam()                   

        elif choice == 'k':
            if son:
                son.stop()
            else:
                print("Pa gen son k'ap jwe.")

        elif choice == 's':
            if son:
                son.stop()
            print("Ou soti nan pwogram nan.")
            break

        else:
            print("Chwa ou fe a pa valab. Tanpri, chwazi yon opsyon ki valab.")

if __name__ == "__main__":
    main()
