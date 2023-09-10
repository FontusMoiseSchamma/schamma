import tkinter as tk
from tkinter import filedialog

def enregistre_fichye():
    tèks = zone_tèks.get("1.0", "end-1c")
    non_fichye = champ_non_fichye.get()

    if tèks.strip() == "" or non_fichye.strip() == "":
        print("Erè: Tèks la oswa non fichye a vid.")
    else:
        with open(non_fichye + ".txt", "w") as fichye:
            fichye.write(tèks)
        print("Fichye enregistre avèk siksè: " + non_fichye + ".txt")

fenet = tk.Tk()
fenet.title("Editè Tèks")
fenet.configure(bg="light yellow")

zone_tèks = tk.Text(fenet, height=15, width=45)
zone_tèks.pack(padx=20, pady=10)

frame = tk.Frame(fenet, bg="light yellow")
frame.pack()

champ_non_fichye = tk.Entry(frame)
champ_non_fichye.pack(side="left")

bouton_enregistre = tk.Button(frame, text="Anrejistre", command=enregistre_fichye, bg="gray",fg="white")
bouton_enregistre.pack(padx=10, pady=10)

fenet.mainloop()
