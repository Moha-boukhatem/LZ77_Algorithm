S= "BRICABRACABRICEDENICE "
new_chaine = ""
chaine = len(S)
gauche = ""
droite = S
i,k = 0,0


# parcour la chaine droite

while i < chaine :

    if len(gauche) >= 9 :
        gauche = gauche[len(gauche)-8:]

    if S[i] in gauche  or  new_chaine !="":
            
        new_chaine += S[i]
        
                   
        if gauche.find(new_chaine) == -1 or len(new_chaine) > 4:
            
           
            new_c = new_chaine[:-1]
            position = len(gauche) - gauche.find(new_c)-1
        

            k+=1    
            print(" {}. gauche = \"{}\" , droite = \"{}\" : code < {} , {} , \"{}\" >".format(k%10,gauche,droite,position,str(len(new_c)),S[i]))
            
            if len(gauche) >= 9 :
                gauche = gauche[len(gauche)-8:]

            gauche += new_chaine
            droite = S[i+1:]
            new_chaine =""

    if S[i] not in gauche  and new_chaine =="":
        k+=1
        print(" {}. gauche = \"{}\" , droite = \"{}\" : code < 0 , 0 , \"{}\" >".format(k,gauche,droite,S[i]))
        gauche+=S[i]
        droite = S[i+1:]

    i+=1

    