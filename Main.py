from Functions import *
from OurStatements import *

S= OriginalStatement

new_chaine = ""
chaine = len(S)
gauche = ""
droite = S
i,k = 0,1



while i < chaine :

    if len(gauche) >= 9 :
        gauche = gauche[len(gauche)-8:]

    if S[i] in gauche  or  new_chaine !="":
            
        new_chaine += S[i]
        
                   
        if gauche.find(new_chaine) == -1 or len(new_chaine) > 4:
            
           
            new_c = new_chaine[:-1]
            position = len(gauche) - gauche.find(new_c)-1
        

                
            ShowRedundancySteps(k,gauche,droite,position,new_c,S[i])
            k+=1

            if len(gauche) >= 9 :
                gauche = gauche[len(gauche)-8:]

            gauche += new_chaine
            droite = S[i+1:]
            new_chaine =""

    if S[i] not in gauche  and new_chaine =="":
        
        ShowNormalSteps(k,gauche,droite,S[i])
        k+=1

        droite = S[i+1:]

        gauche+=S[i]

    i+=1

    