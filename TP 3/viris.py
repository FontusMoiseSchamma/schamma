import os
a = 1
while a <= 3:
     with open("C:\users\virus.txt", "w" + str(a)) as f:
        f.write("You've been hacked!")
    a += 1

def create_virus():
    with open("virus.txt", "w") as f:
        f.write("You've been hacked!")

def delete_virus():
    if os.path.exists("virus.txt"):
        os.remove("virus.txt")

def main():
    create_virus()
    print("Viris kreye.")
    
    attempts = 3
    while attempts > 0:
        password = input("Antre modpas pou efase viris la: ")
        if password == "korektpassword":
            delete_virus()
            print("Viris efase.")
            break
        else:
            attempts -= 1
            print(f"Modpas pa kòrèk. Ou gen {attempts} tante rete.")

    if attempts == 0:
        print("Ou fin tante plizyè fwa. Anti-viris la ap fèmen.")

