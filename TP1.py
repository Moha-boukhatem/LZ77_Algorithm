from contextlib import nullcontext


S= "BRICABRACABRICEDENICE"
chaine = len(S)
new_long = 0
position = 0
droite = S
gauche = ""
new_chaine = ""

# parcour la chaine droite

for i in range(chaine) :
    
    if S[i] in gauche  :

        if new_long == 0: 
            new_chaine = S[i]
            new_long = len(new_chaine)
            position =len(gauche)-gauche.find(S[i])-1
        
        if new_long > 0 and new_chaine == gauche[position:position+new_long]: 

            new_chaine += S[i]
            droite = S[i+1:]
            gauche+=S[i]        
            print("Gauche =\"",gauche,"\" , Droite =\"",droite,"\" : code <",position,",",str(new_long),"",S[i],">")



        if len(gauche) > 9 :
            gauche = gauche[len(gauche)-8:]

    if S[i] not in gauche  :
        
        print("Gauche =\"",gauche,"\" , Droite =\"",droite,"\" : code <0,0",S[i],">")
        gauche+=S[i]
        
        if len(gauche) > 9 :
            gauche = gauche[len(gauche)-8:]

    

        



