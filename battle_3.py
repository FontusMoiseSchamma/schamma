def kalkile_pòt_ouvri(adres_IP):
    sousadres = adres_IP.split('.')
    chif_yo = [int(sousadr) for sousadr in sousadres]
    total = sum(chif_yo)
    premye_sousadr = chif_yo[0]
    pòt_ouvri = total * premye_sousadr
    return pòt_ouvri

adres_IP = input("Antre adres IP a (separe ak pon): ")

pòt_ouvri = kalkile_pòt_ouvri(adres_IP)

print(f"{adres_IP} ap bay rezilta")
print(f"({'+'.join(adres_IP.split('.'))}) * {adres_IP[0]} = {pòt_ouvri}")
print(f"Donk pòt ki ouvri a se {pòt_ouvri}")
