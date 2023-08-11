a=0
b=3
kantite=[1,2,3,4,5,6,7,8,9,10]
chwa_1="w"
chwa_2="n"

print("Tab miltiplikasyon")

while(a<b):
    nonb_chwazi=int(input("Antre yon nonb :"))
    for c in kantite:
        print(nonb_chwazi,"* ",c,"=",nonb_chwazi*c)
    desizyon=str(input("Peze (w) siw bezwen yon lot tab miltiplikasyon, peze (n) si ou pa bezwen yon tap miltiplikasyon :"))
    if(desizyon==chwa_1):
        continue
    if(desizyon==chwa_2):
        print("OK :)")
        break
