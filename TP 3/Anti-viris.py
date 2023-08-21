from viris import delete_virus

def main():
    create_virus()
    print("Viris kreye.")
    
    chans = 3
    while chans > 0:
        password = input("Antre modpas pou efase viris la: ")
        if password == "korektpassword":
            delete_virus()
            print("Viris efase.")
            break
        else:
            chans -= 1
            print(f"Modpas pa kòrèk. Ou gen {attempts} tante rete.")

    if chans == 0:
        print("Ou fin tante plizyè fwa. Anti-viris la ap fèmen.")

