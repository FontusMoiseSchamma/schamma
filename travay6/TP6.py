import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

conn = sqlite3.connect('baz_done.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL UNIQUE,password TEXT NOT NULL)")

# Kreye yon tablo "income" pou stoke done REVNI yo (si li pa egziste li pral kreye li)
cursor.execute("CREATE TABLE IF NOT EXISTS income (income_id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER NOT NULL,montan REAL NOT NULL,kategori TEXT NOT NULL,dat DATE NOT NULL,deskripsyon TEXT,FOREIGN KEY (user_id) REFERENCES users (user_id))")

# Kreye yon tablo "expenses" pou stoke done DEPANS yo (si li pa egziste li pral kreye li)
cursor.execute("CREATE TABLE IF NOT EXISTS expenses (expense_id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER NOT NULL,amount REAL NOT NULL,category TEXT NOT NULL,date DATE NOT NULL,description TEXT,FOREIGN KEY (user_id) REFERENCES users (user_id))")

# Kreye yon tablo "budgets" pou stoke done sou bidjè itilizatè yo (si li pa egziste li pral kreye li)
cursor.execute("CREATE TABLE IF NOT EXISTS budgets (budget_id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER NOT NULL,category TEXT NOT NULL,amount REAL NOT NULL,FOREIGN KEY (user_id) REFERENCES users (user_id))")

# Fonksyon pou tcheke si yon dat nan fòma kòrèk (DD-MM-YYYY)
def valide_dat(dat):
    # Kreye yon patèn regex pou kòrdine ak dat nan fòma "DD-MM-YYYY"
    regex_patèn = r"\d{2}-\d{2}-\d{4}"

    # Tcheke si dat la kòrèk selon patèn nan
    if re.match(regex_patèn, dat):
        return True
    else:
        return False

# Fonksyon pou ajoute yon nouvo REVNI
def ajoute_revni(revni_entry, revni_kategori, revni_dat, revni_deskripsyon):
    global utilizatè_id
    if utilizatè_id is None:
        messagebox.showerror("Erè", "Otantifye avan ou ajoute REVNI.")
        return

    montan_input = revni_entry.get()
    if not montan_input:
        messagebox.showerror("Erè", "Antre yon montan pou REVNI.")
        return

    montan = float(revni_entry.get())
    kategori = revni_kategori.get()
    dat = revni_dat.get()
    deskripsyon = revni_deskripsyon.get("1.0", tk.END)

    if montan <= 0 or kategori == "" or dat == "":
        messagebox.showerror("Erè", "Ranpli tout fòm yo ak montan pozitif.")
        return

    if not valide_dat(dat):
        messagebox.showerror("Erè", "Fòma dat la pa kòrèk. Itilize fòma DD-MM-YYYY.")
        return

    conn = sqlite3.connect('baz_done.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO income (user_id, montan, kategori, dat, deskripsyon) VALUES (?, ?, ?, ?, ?)",(utilizatè_id, montan, kategori, dat, deskripsyon))
    conn.commit()
    conn.close()

    revni_entry.delete(0, tk.END)
    revni_kategori.set("")
    revni_dat.set("")
    revni_deskripsyon.delete("1.0", tk.END)

# Fonksyon pou ajoute yon nouvo DEPANS
def ajoute_depans(depans_entry, depans_kategori, depans_date, depans_description):
    if utilizatè_id is None:
        messagebox.showerror("Erè", "Otantifikasyon sezi. Otantifye avan ou ajoute DEPANS.")
        return

    depans_input = depans_entry.get()
    if not depans_input:
        messagebox.showerror("Erè", "Antre yon montan pou DEPANS.")
        return

    montan = float(depans_entry.get())
    kategori = depans_kategori.get()
    dat = depans_date.get()
    deskripsyon = depans_description.get("1.0", tk.END)

    if montan <= 0 or kategori == "" or dat == "":
        messagebox.showerror("Erè", "Ranpli tout fòm yo ak montan pozitif.")
        return

    if not valide_dat(dat):
        messagebox.showerror("Erè", "Fòma dat la pa kòrèk. Itilize fòma DD-MM-YYYY.")
        return

    conn = sqlite3.connect('baz_done.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",(utilizatè_id, montan, kategori, dat, deskripsyon))
    conn.commit()
    conn.close()

    depans_entry.delete(0, tk.END)
    depans_kategori.set("")
    depans_date.set("")
    depans_description.delete("1.0", tk.END)

# Fonksyon pou ajoute bidjè yo nan baz done
# Fonksyon pou ajoute bidjè yo nan baz done
def ajoute_bidje(kategori, montan, kategori_entry, montan_entry):
    global utilizatè_id
    if utilizatè_id is None:
        messagebox.showerror("Erè", "Otantifye avan ou ajoute bidjè.")
        return

    if not kategori or not montan:
        messagebox.showerror("Erè", "Antre yon kategori ak yon montan pou bidjè a.")
        return

    montan = float(montan)

    # Konekte nan baz done
    conn = sqlite3.connect('baz_done.db')
    cursor = conn.cursor()
    # Ekzekite yon kòmand SQL pou ajoute bidjè a nan tablo "budgets"
    cursor.execute("INSERT INTO budgets (user_id, category, amount) VALUES (?, ?, ?)", (utilizatè_id, kategori, montan))
    conn.commit()
    # Fèmen konksyon an
    conn.close()

    messagebox.showinfo("Siksè", "Bidjè a ajoute avèk siksè.")

    # Wipe zòn antre yo
    kategori_entry.delete(0, tk.END)
    montan_entry.delete(0, tk.END)


# Fonksyon pou jenere rapò finansye
def jenere_rapò_finansye():
    global fenet_rapò
    if fenet_rapò is not None and fenet_rapò.winfo_exists():
        fenet_rapò.destroy()
        
    global utilizatè_id
    if utilizatè_id is None:
        messagebox.showerror("Erè", "Otantifye avan ou jenere rapò finansye.")
        return

    montan = 0.0

    # Konekte nan baz done
    conn = sqlite3.connect('baz_done.db')
    cursor = conn.cursor()

    # Kalkile total revni itilizatè a
    cursor.execute("SELECT SUM(montan) FROM income WHERE user_id=?", (utilizatè_id,))
    total_revni = cursor.fetchone()[0] or 0.0

    # Kalkile total depans itilizatè a
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE user_id=?", (utilizatè_id,))
    total_depans = cursor.fetchone()[0] or 0.0

    # Jwenn lis revni itilizatè a
    cursor.execute("SELECT montan, kategori, dat FROM income WHERE user_id=?", (utilizatè_id,))
    revni_records = cursor.fetchall()

    # Jwenn lis depans itilizatè a
    cursor.execute("SELECT amount, category, date FROM expenses WHERE user_id=?", (utilizatè_id,))
    depans_records = cursor.fetchall()

    # Jwenn lis bidjè itilizatè a
    cursor.execute("SELECT category, amount FROM budgets WHERE user_id=?", (utilizatè_id,))
    bidje_records = cursor.fetchall()

    # Fèmen konksyon an
    conn.close()

    # Kreye yon fenèt Toplevel pou afiche rapò finansye a
    fenet_rapò = tk.Toplevel()
    fenet_rapò.title("Rapò Finansye")
    fenet_rapò.geometry("650x750")
    fenet_rapò.configure(bg="#E6E6FA")

     # Kreye yon etikèt pou afiche non itilizate nan fraz la
    username_label = tk.Label(fenet_rapò, text=f"Rapo finansye *{username}*", font=("Helvetica", 18))
    username_label.pack()
    username_label.configure(bg="#E6E6FA")


    # Ajoute detay sou revni yo nan fenèt la
    revni_frame = tk.LabelFrame(fenet_rapò, text="Detay REVNI", font=("Helvetica", 16))
    revni_frame.pack(fill="both", expand="yes", padx=20, pady=10)
    revni_frame.configure(bg="#E6E6FA")

    for record in revni_records:
        montan, kategori, dat = record
        revni_detail_label = tk.Label(revni_frame, text=f"Montan: ${montan:.2f}, Kategori: {kategori}, Dat: {dat}", font=("Calibri", 10))
        revni_detail_label.pack()
        revni_detail_label.configure(bg="#E6E6FA")

    # Ajoute detay sou depans yo nan fenèt la
    depans_frame = tk.LabelFrame(fenet_rapò, text="Detay DEPANS", font=("Helvetica", 16))
    depans_frame.pack(fill="both", expand="yes", padx=20, pady=10)
    depans_frame.configure(bg="#E6E6FA")

    for record in depans_records:
        amount, kategori, dat = record
        depans_detail_label = tk.Label(depans_frame, text=f"Montan: ${amount:.2f}, Kategori: {kategori}, Dat: {dat}", font=("Calibri", 10))
        depans_detail_label.pack()
        depans_detail_label.configure(bg="#E6E6FA")

    # Ajoute detay sou bidjè yo nan fenèt la
    bidje_frame = tk.LabelFrame(fenet_rapò, text="Detay BIDJÈ", font=("Helvetica", 16))
    bidje_frame.pack(fill="both", expand="yes", padx=20, pady=10)
    bidje_frame.configure(bg="#E6E6FA")

    for record in bidje_records:
        kategori, montan = record
        bidje_detail_label = tk.Label(bidje_frame, text=f"Kategori: {kategori}, Montan: ${montan:.2f}", font=("Calibri", 10))
        bidje_detail_label.pack()
        bidje_detail_label.configure(bg="#E6E6FA")

    # Ajoute kontni rapò finansye a nan fenèt la
    # Ajoute detay sou bidjè yo nan fenèt la
    rapò_label = tk.LabelFrame(fenet_rapò, text="Rapò Finansye", font=("Helvetica", 16))
    rapò_label.pack(fill="both", expand="yes", padx=20, pady=10)
    rapò_label.configure(bg="#E6E6FA")
    
    revni_label = tk.Label(rapò_label, text=f"Total REVNI: ${total_revni:.2f}", font=("Calibri", 10))
    revni_label.pack()
    revni_label.configure(bg="#E6E6FA")

    depans_label = tk.Label(rapò_label, text=f"Total DEPANS: ${total_depans:.2f}", font=("Calibri", 10))
    depans_label.pack()
    depans_label.configure(bg="#E6E6FA")

    bilan_label = tk.Label(rapò_label, text=f"Bilan: ${total_revni - total_depans:.2f}", font=("Calibri", 10))
    bilan_label.pack()
    bilan_label.configure(bg="#E6E6FA")

    # Kreye yon bouton pou referme fenèt la
    fenet_fèmen_bouton = tk.Button(fenet_rapò, text="Fèmen", font=("Arial", 14), command=fenet_rapò.destroy)
    fenet_fèmen_bouton.pack()

# Fonksyon pou kreye ak afiche fenèt aplikasyon an
def open_main_window():
    main_window = tk.Tk()
    main_window.title("CashFlow Master - Aplikasyon")
    main_window.geometry("650x750")
    main_window.configure(bg="#E6E6FA")

     # Kreye yon etikèt pou afiche non itilizate nan fraz la
    message_label = tk.Label(main_window, text=f"Byenveni *{username}* nan CashFlow Master!", font=("Helvetica", 18))
    message_label.pack()
    message_label.configure(bg="#E6E6FA")
    
    # Kreye yon kadri nan fenèt la pou ajoute REVNI
    revni_frame = tk.LabelFrame(main_window, text="Ajoute REVNI", font=("Helvetica", 16))
    revni_frame.pack(fill="both", expand="yes", padx=20, pady=10)
    revni_frame.configure(bg="#E6E6FA")

    # Kreye etikèt ak zòn antre pou montant REVNI
    revni_label = tk.Label(revni_frame, text="Montan:", font=("Calibri", 10))
    revni_label.grid(row=0, column=0)
    revni_label.configure(bg="#E6E6FA")
    revni_entry = tk.Entry(revni_frame, font=("Verdana", 12))
    revni_entry.grid(row=0, column=1)

    # Kreye etikèt ak zòn antre pou kategori REVNI
    revni_kategori = tk.StringVar()
    revni_kategori.set("")  # Kategori a pou REVNI
    revni_kategori_label = tk.Label(revni_frame, text="Kategori:", font=("Calibri", 10))
    revni_kategori_label.grid(row=1, column=0)
    revni_kategori_label.configure(bg="#E6E6FA")
    revni_kategori_menu = tk.OptionMenu(revni_frame, revni_kategori, "Salè", "Lòt")
    revni_kategori_menu.grid(row=1, column=1)

    # Kreye etikèt ak zòn antre pou dat REVNI
    revni_date = tk.StringVar()
    revni_date.set("")  # Dat la pou REVNI
    revni_date_label = tk.Label(revni_frame, text="Dat:", font=("Calibri", 10))
    revni_date_label.grid(row=2, column=0)
    revni_date_label.configure(bg="#E6E6FA")
    revni_date_entry = tk.Entry(revni_frame, font=("Verdana", 12), textvariable=revni_date)
    revni_date_entry.grid(row=2, column=1)

    # Kreye etikèt ak zòn antre pou deskripsyon REVNI
    revni_description_label = tk.Label(revni_frame, text="Deskripsyon:", font=("Calibri", 10))
    revni_description_label.grid(row=3, column=0)
    revni_description_label.configure(bg="#E6E6FA")
    revni_description = tk.Text(revni_frame, font=("Calibri", 10), height=5, width=30)
    revni_description.grid(row=3, column=1)

    # Kreye bouton pou ajoute REVNI
    ajoute_revni_button = tk.Button(revni_frame, text="Ajoute Revni", font=("Arial", 14), command=lambda: ajoute_revni(revni_entry, revni_kategori, revni_date, revni_description))
    ajoute_revni_button.grid(row=4, columnspan=2)

    # Kreye yon kadri nan fenèt la pou ajoute DEPANS
    depans_frame = tk.LabelFrame(main_window, text="Ajoute DEPANS", font=("Helvetica", 16))
    depans_frame.pack(fill="both", expand="yes", padx=20, pady=10)
    depans_frame.configure(bg="#E6E6FA")

    # Kreye etikèt ak zòn antre pou montant DEPANS
    depans_label = tk.Label(depans_frame, text="Montan:", font=("Calibri", 10))
    depans_label.grid(row=0, column=0)
    depans_label.configure(bg="#E6E6FA")
    depans_entry = tk.Entry(depans_frame, font=("Verdana", 12))
    depans_entry.grid(row=0, column=1)

    # Kreye etikèt ak zòn antre pou kategori DEPANS
    depans_kategori = tk.StringVar()
    depans_kategori.set("")  # Kategori a pou DEPANS
    depans_kategori_label = tk.Label(depans_frame, text="Kategori:", font=("Calibri", 10))
    depans_kategori_label.grid(row=1, column=0)
    depans_kategori_label.configure(bg="#E6E6FA")
    depans_kategori_menu = tk.OptionMenu(depans_frame, depans_kategori, "Manje", "Lòt")
    depans_kategori_menu.grid(row=1, column=1)

    # Kreye etikèt ak zòn antre pou dat DEPANS
    depans_date = tk.StringVar()
    depans_date.set("")  # Dat la pou DEPANS
    depans_date_label = tk.Label(depans_frame, text="Dat:", font=("Calibri", 10))
    depans_date_label.grid(row=2, column=0)
    depans_date_label.configure(bg="#E6E6FA")
    depans_date_entry = tk.Entry(depans_frame, font=("Verdana", 12), textvariable=depans_date)
    depans_date_entry.grid(row=2, column=1)

    # Kreye etikèt ak zòn antre pou deskripsyon DEPANS
    depans_description_label = tk.Label(depans_frame, text="Deskripsyon:", font=("Calibri", 10))
    depans_description_label.grid(row=3, column=0)
    depans_description_label.configure(bg="#E6E6FA")
    depans_description = tk.Text(depans_frame, font=("Calibri", 10), height=5, width=30)
    depans_description.grid(row=3, column=1)

    # Kreye bouton pou ajoute DEPANS
    ajoute_depans_button = tk.Button(depans_frame, text="Ajoute Depans", font=("Arial", 14), command=lambda: ajoute_depans(depans_entry, depans_kategori, depans_date, depans_description))
    ajoute_depans_button.grid(row=4, columnspan=2)

    # Kreye yon kadri nan fenèt la pou ajoute bidjè
    bidje_frame = tk.LabelFrame(main_window, text="Ajoute Bidjè", font=("Helvetica", 16))
    bidje_frame.pack(fill="both", expand="yes", padx=20, pady=10)
    bidje_frame.configure(bg="#E6E6FA")

    # Kreye etikèt ak zòn antre pou kategori bidjè
    bidje_kategori = tk.StringVar()
    bidje_kategori.set("")  # Kategori a pou bidjè
    bidje_kategori_label = tk.Label(bidje_frame, text="Kategori:", font=("Calibri", 10))
    bidje_kategori_label.grid(row=0, column=0)
    bidje_kategori_label.configure(bg="#E6E6FA")
    bidje_kategori_entry = tk.Entry(bidje_frame, font=("Verdana", 12), textvariable=bidje_kategori)
    bidje_kategori_entry.grid(row=0, column=1)

    # Kreye etikèt ak zòn antre pou montan bidjè
    bidje_montan = tk.StringVar()
    bidje_montan.set("")  # Montan an pou bidjè
    bidje_montan_label = tk.Label(bidje_frame, text="Montan:", font=("Calibri", 10))
    bidje_montan_label.grid(row=1, column=0)
    bidje_montan_label.configure(bg="#E6E6FA")
    bidje_montan_entry = tk.Entry(bidje_frame, font=("Verdana", 12), textvariable=bidje_montan)
    bidje_montan_entry.grid(row=1, column=1)

    # Kreye bouton pou ajoute bidjè
    ajoute_bidje_button = tk.Button(bidje_frame, text="Ajoute Bidjè", font=("Arial", 14), command=lambda: ajoute_bidje(bidje_kategori_entry.get(), bidje_montan_entry.get(), bidje_kategori_entry, bidje_montan_entry))
    ajoute_bidje_button.grid(row=2, columnspan=2)

    # Kreye bouton pou jenere rapò finansye
    jenere_rapò_button = tk.Button(main_window, text="Jenere Rapò Finansye", font=("Arial", 14), command=jenere_rapò_finansye)
    jenere_rapò_button.pack()

    main_window.mainloop()

# Fonksyon pou kreye yon nouvo kont
def kreye_nouvo_kont():
    global fenet_kreye_kont
    if fenet_kreye_kont is not None and fenet_kreye_kont.winfo_exists():
        fenet_kreye_kont.destroy()
        
    fenet_kreye_kont = tk.Toplevel()
    fenet_kreye_kont.title("Kreye Nouvo Kont")
    fenet_kreye_kont.geometry("400x150")
    fenet_kreye_kont.configure(bg="#E6E6FA")

    label_username = tk.Label(fenet_kreye_kont, text="Username:", font=("Calibri", 10))
    label_username.pack()
    label_username.configure(bg="#E6E6FA")

    entry_username = tk.Entry(fenet_kreye_kont, font=("Verdana", 12))
    entry_username.pack()

    label_password = tk.Label(fenet_kreye_kont, text="Password:", font=("Calibri", 10))
    label_password.pack()
    label_password.configure(bg="#E6E6FA")

    entry_password = tk.Entry(fenet_kreye_kont, show="*")
    entry_password.pack()

    bouton_kreye = tk.Button(fenet_kreye_kont, text="Kreye Kont", font=("Arial", 14), command=lambda: sauv_registrasyon(entry_username.get(), entry_password.get()))
    bouton_kreye.pack()

# Fonksyon pou sove nouvo kont nan baz done
def sauv_registrasyon(username, password):
    if not username or not password:
            messagebox.showerror("Erè", "Antre yon username ak yon modpas avan ou kreye kont.")
            return
        
    conn = sqlite3.connect('baz_done.db')
    cursor = conn.cursor()

    # Verifikasyon si username deja egziste nan baz done a
    cursor.execute("SELECT user_id FROM users WHERE username=?", (username,))
    result = cursor.fetchone()

    if result is not None:
        messagebox.showerror("Erè", "Username sa deja egziste. Chwazi yon lòt username.")
        conn.close()
    else:
        # Ajoute nouvo itilizatè nan baz done
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Siksè", "Kont la kreye avèk siksè.")
        fenet_kreye_kont.destroy()

    fenet_kreye_kont.mainloop()
# Kreye yon variab global pou id itilizatè a
utilizatè_id = None
fenet_kreye_kont = None
fenet_rapò = None

# Kreye fenèt otantifikasyon an
fenet = tk.Tk()
fenet.title("CashFlow Master - Otantifikasyon")
fenet.geometry("450x250")
fenet.configure(bg="#E6E6FA")

username = ""

# Fonksyon pou otantifye itilizatè a
def otantifye():
    global username
    # Kòmanse ak posisyon 1.0 nan zòn teks la, ak pran tout kontni a rive nan fenèt la
    username = otantifikasyon_username.get()
    password = otantifikasyon_password.get()

    if not username or not password:
        messagebox.showerror("Erè", "Antre username ak password avan ou otantifye.")
        return

    # Verifye si username ak modpas yo koresponn ak done nan baz done yo
    conn = sqlite3.connect('baz_done.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()

    if result is not None:
        # Otantifikasyon sezi, asiyen id itilizatè a nan variab "utilizatè_id"
        global utilizatè_id
        utilizatè_id = result[0]

        # Fèmen fenèt otantifikasyon an
        fenet.destroy()
        
        open_main_window()
    else:
        messagebox.showerror("Erè", "Tantativ otantifikasyon echwe.\nOu ka kreye yon nouvo kont si ou pa genyen yon kont deja.")
        # Efase kontni nan zòn antre yo
        otantifikasyon_username.delete(0, tk.END)
        otantifikasyon_password.delete(0, tk.END)


# Kreye yon kadri nan fenèt la pou otantifikasyon
otantifikasyon_frame = tk.LabelFrame(fenet, text="Otantifikasyon", font=("Helvetica", 16))
otantifikasyon_frame.pack(fill="both", expand="yes", padx=20, pady=10)
otantifikasyon_frame.configure(bg="#E6E6FA")

# Kreye etikèt ak zòn antre pou username nan otantifikasyon
otantifikasyon_username_label = tk.Label(otantifikasyon_frame, text="Username:", font=("Calibri", 10))
otantifikasyon_username_label.grid(row=1, column=0)
otantifikasyon_username_label.configure(bg="#E6E6FA")
otantifikasyon_username = tk.Entry(otantifikasyon_frame, font=("Verdana", 12))
otantifikasyon_username.grid(row=1, column=1)

# Kreye etikèt ak zòn antre pou modpas nan otantifikasyon
otantifikasyon_password_label = tk.Label(otantifikasyon_frame, text="Password:", font=("Calibri", 10))
otantifikasyon_password_label.grid(row=2, column=0)
otantifikasyon_password_label.configure(bg="#E6E6FA")
otantifikasyon_password = tk.Entry(otantifikasyon_frame, show="*")
otantifikasyon_password.grid(row=2, column=1)

# Kreye bouton pou otantifye
otantifikasyon_bouton = tk.Button(otantifikasyon_frame, text="Otantifye", font=("Arial", 12), command=otantifye)
otantifikasyon_bouton.grid(row=3, columnspan=2)

# Kreye yon bouton pou kreye yon nouvo kont
bouton_kreye_kont = tk.Button(otantifikasyon_frame, text="Kreye Nouvo Kont", font=("Arial", 12), command=kreye_nouvo_kont)
bouton_kreye_kont.grid(row=4, columnspan=2)

# Kòmanse aplikasyon an
conn.commit()
# Fèmen konksyon an
conn.close()

# Lanse aplikasyon an
fenet.mainloop()
