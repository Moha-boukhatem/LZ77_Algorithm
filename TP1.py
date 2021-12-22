S= "BRICABRACABRICEDENICE"
new_chaine = ""
chaine = len(S)
gauche = ""
droite = S
i = 0



'''
position = 0
droite = S
'''
# parcour la chaine droite

while i < chaine :

    if len(gauche) >= 9 :
        gauche = gauche[len(gauche)-8:]

    if S[i] in gauche  :
            
        new_chaine += S[i]
        
        position = len(gauche) - gauche.find(new_chaine)-2 
        
        if gauche.find(new_chaine) == -1 :
            
            gauche += new_chaine
            if len(gauche) >= 9 :
                gauche = gauche[len(gauche)-8:]
            print("Gauche =\"",gauche,"\" , Droite =\"",droite,"\" : code <",position,",",str(len(new_chaine)),"",S[i],">")
            droite = S[i+1:]
            new_chaine =""



        '''
         
            
            len(new_chaine) = len(new_chaine)
            position =len(gauche)-gauche.find(S[i])-1
        
         and new_chaine == gauche[position:position+len(new_chaine)]: 

            new_chaine += S[i]
            droite = S[i+1:]
            gauche+=S[i]        
        '''
        
    if S[i] not in gauche  :
        print("Gauche =\"",gauche,"\" , Droite =\"",droite,"\" : code < 0 , 0 ",S[i],">")
        gauche+=S[i]
        droite = S[i+1:]

    i+=1

    

    

        



