total= 0
while True:
    umur= int(input ("Masukkan umur anda, 00 untuk berhenti: "))
    if umur == 00:
        break
    if umur <= 2: 
        harga = 0 
        print("gratis")
    elif 3 <= umur <= 12:
        harga= 14.00
        print("harganya $14.00")
    elif umur >= 65:
        harga = 18
        print ("harganya $18.00")
    else:
        harga = 23
        print ("harganya $23.00")
     
    total+= harga
    print (f"running total : {total:.2f}")
    
uang= float(input("masukkan uang anda: "))
if uang< total:
    print("kurang der duitlu")
elif uang>= total:
    kembalian = uang- total
    print (f"uang kembali {kembalian:.2f}")

