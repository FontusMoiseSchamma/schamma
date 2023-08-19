panye = []

def ajoute_nan_panye(pwodwi,panye):
    a=0
    b=1
    while b >0 :
      num = int(input("Tape numero pwodwi ou vle mete nan panye ou an :"))
      kantite = int(input("Tape kantite ou vle nan pwodwi sa:"))
      if 1 <= num <= len(pwodwi):
        panye.append(pwodwi[num-1])
        panye[a]['Quantity'] = kantite
        a+=1
      try:  
        c = str(input("Tape (n) si ou pap mete nan panye ou a anko, epi tape nenpot lot let si wap mete toujou :"))
        if c == "n":
          break 
        else:
          continue 
      except ValueError:
         c = str(input('Tape on let: '))
         
def kalkile_pri_total():
    total = 0
    for pwodwi_lis in panye:
        total += pwodwi_lis["Price"]
    return total
#mta renmen jwenn yon solisyon pou som nan silvouple
