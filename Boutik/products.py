pwodwi_lis = [{"Name": "Laptop", "Price": 15000, "Quantity":200},
              {"Name": "Tablet", "Price": 9000, "Quantity":100},
              {"Name": "Telefon", "Price": 5000, "Quantity":1500},
              {"Name": "Backup", "Price": 2000, "quantity":200},
              ]

def afiche_pwodwi(l):
    print("Men pwodwi ki disponib yo:")
    a=0
    for b in pwodwi_lis:
        a=a+1
        print(a,b)
