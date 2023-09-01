import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame
import time

pygame.init()
pygame.mixer.init()

son = None

def alam():
    print("\nAlam! Alam! Alam! Alam! Alam!")
    global son
    if son:
        son.play()
    else:
        print("Pa gen son alam. Tanpri, chwazi yon son k ap jwe kòm alam.")

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
            print("Odinate a ap fèmen ...")
            time.sleep(2) 
            os.system("shutdown /s /t 1")

        elif choice == 'r':
            print("Odinate a ap redemare ...")
            time.sleep(2)
            os.system("shutdown /r /t 1")
            
        elif choice == 'a':
            if son:
                son.stop()  # Kanpe son an si te gen yon son ki tap jwe

            son_path = input("Antre chemen dosye son alam ou: ")
            if os.path.exists(son_path):
                son = pygame.mixer.Sound(son_path)
                alam()  # Jwe son alam
            else:
                print("Dosye son pa egziste.")

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
