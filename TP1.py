S = "BRICABRACABRICEDENICE"

gauche = ""
droite = S
new_chaine = ""
# parcour la chaine droite

for i in S :
    
    if  i not in gauche :

        print("Gauche =",gauche," , Droite =",droite," : code <0,0,",i,">")
        gauche+=i
        droite = droite[1:]


    else :
        new_chaine += i
        print("Gauche =",gauche," , Droite =",droite," : code <",len(gauche)-gauche.find(i),",",len(new_chaine),"",i,">")

