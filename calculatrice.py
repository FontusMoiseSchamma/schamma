import tkinter as tk
from tkinter import ttk

# mwen ajoute 2 varyab poum k jere pwen an
operateur_utilize = False
point_utilize = False  

def evaluer():
    global operateur_utilize
    global point_utilize  
    
    try:
        expression = entry.get()
        expression = expression.replace(',', '.')
        resultat = eval(expression)
        label_resultat.config(text="Résultat : " + str(resultat))
        entry.delete(0, tk.END)
        
        operateur_utilize = False
    except Exception as e:
        label_resultat.config(text="Erreur")
        entry.delete(0, tk.END)

def ajoute_caractere(caractere):
    global operateur_utilize
    global point_utilize
    
    if caractere in ['+', '-', '*', '/']:
        if operateur_utilize:
            return
        operateur_utilize = True
        
        point_utilize = False
    
    if caractere == '.' and point_utilize:
        return
    
    entry.insert(tk.END, caractere)
    
    if caractere == '.':
        point_utilize = True
    elif caractere.isdigit() or caractere in ['+', '-', '*', '/']:
        operateur_utilize = False

fenet = tk.Tk()
fenet.title("Calculatrice")
fenet.geometry("200x250")

entry = tk.Entry(fenet)
entry.config(font=("Arial", 10), bg="yellow", fg="black")
entry.grid(row=0, column=0, columnspan=4, sticky='ew')

label_resultat = tk.Label(fenet, text="",font=("Helvetica", 10), bg="lightgray", fg="black")
label_resultat.grid(row=1, column=0, columnspan=4, sticky='ew')

custom_style = ttk.Style()
custom_style.configure('Custom.TButton', background='yellow')

boutons = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '0', '.', '=', '/']

ligne = 2
colonne = 0

for bouton in boutons:
    if bouton == '=':
        ttk.Button(fenet, text=bouton, width=5, style='Custom.TButton', command=evaluer).grid(row=ligne, column=colonne, sticky='nsew')
    else:
        ttk.Button(fenet, text=bouton, width=5, style='Custom.TButton', command=lambda b=bouton: ajoute_caractere(b)).grid(row=ligne, column=colonne, sticky='nsew')

    colonne += 1
    if colonne > 3:
        colonne = 0
        ligne += 1

for i in range(4):
    fenet.grid_columnconfigure(i, weight=1)
    fenet.grid_rowconfigure(i + 2, weight=1)

fenet.mainloop()
