# CODED BY PÂYİDAR

boy = float(input("Boy:"))
kilo = int(input("Kilo:"))

endeks  = kilo/(boy**2)

if endeks<18.5:
    print("n Zayıf")
elif endeks > 18.5 and endeks <=25 :
    print("n Normal")
elif endeks > 25 and endeks <=30:
    print("n Kilolu")
elif endeks > 30:
    print("n Obez")
