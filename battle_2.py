def se_palendwom(chenn):
    chenn = chenn.lower()  
    chenn = chenn.replace(" ", "")  

    return chenn == chenn[::-1]  

chenn_test = input("Antre yon chenn: ")

if se_palendwom(chenn_test):
    print("Se yon palendwòm.")
else:
    print("Pa se yon palendwòm.")
