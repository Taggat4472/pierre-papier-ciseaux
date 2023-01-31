
import random

while True :
    choix=["papier ","pierre","ciseaux"]
    ordi=random.choice(choix)
    moi = None
    while moi not in choix :
        moi =input("papier,pierre,ciseaux?: ").lower()
        if moi == ordi:
            print("ordi:",ordi)
            print("moi:",moi)
            print ("égalité")
        
        elif moi == "papier" :
            if ordi == "pierre":
                print("ordi:",ordi)
                print("moi:",moi)
                print("gagné")
            if ordi == "ciseaux":
                print("ordi:",ordi)
                print("moi:",moi)
                print("perdu")
                
        elif moi == "pierre" :
            if ordi == "ciseaux":
                print("ordi:",ordi)
                print("moi:",moi)
                print("gagné")
            if ordi == "papier":
                print("ordi:",ordi)
                print("moi:",moi)
                print("perdu")
                 
        elif moi == "ciseaux" :
            if ordi == "papier":
                print("ordi:",ordi)
                print("moi:",moi)
                print("gagné")
            if ordi == "pierre":
                print("ordi:",ordi)
                print("moi:",moi)
                print("perdu")
            
        
       
    rejouer=input("voulez rejouer?(oui/non):").lower()
    if rejouer != "oui":
        break
         
