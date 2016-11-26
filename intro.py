print("Hello "+"World!")
print(1!=78 or 59<12)

if 25>=35:
    print("Yess")
else: print("Noo!!")

Name="Niki"
if Name=="Niki":
    print("Szia Niki!")
elif Name=="Orsi":
    print("Szia Orsi!")
else: print("Szia Zuzsi!")

volume=15
if volume<20:
    print("kicsit halk")
elif volume >=20 and volume <40:
    print("fasza hatterzene")
elif volume >=40 and volume <60:
    print("tokeletes")
elif volume >=60 and volume <80:
    print("kicsit hangos")
else: print("!!!")



def func(name):
    print ("Szia "+name+"!")
list=["Niki","Gyorgyi","Orsi", "Zsuzsi"]
for n in list:
    func(n)
for n in range(1,10):
    print (n)
