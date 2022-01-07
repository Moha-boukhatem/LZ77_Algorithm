from PrintFunctions import *
import Statements as Statements

def Main():
    #LZ77_Compression_Function(Statements.OriginalStatement)

    
    LZ77_Decompression_Function(Statements.OriginalStatement)



def LZ77_Compression_Function(Statement):
    
    gauche_list ,droite_list ,position_list ,size_list ,lettre_list= [],[],[],[],[]
    print("\n ##################    Message Encoding   ##################\n")

    PrintStatement(Statement)

    S= Statement
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
        
                position_list.append(position)
                size_list.append(len(new_c))
                lettre_list.append(S[i])

                k+=1

                if len(gauche) >= 9 :
                    gauche = gauche[len(gauche)-8:]

                gauche += new_chaine
                droite = S[i+1:]
                new_chaine =""

        if S[i] not in gauche  and new_chaine =="":
            
            ShowNormalSteps(k,gauche,droite,S[i])
            gauche_list.append(gauche)
            droite_list.append(droite)
            position_list.append(0)
            size_list.append(0)
            lettre_list.append(S[i])

            k+=1

            droite = S[i+1:]
            gauche+=S[i]

        i+=1

    return position_list ,size_list ,lettre_list
def LZ77_Decompression_Function(Statement):

    data = LZ77_Compression_Function(Statement)
    
    print("\n ##################    Message Decoding    ##################\n")
 
    position_list = data[0]
    size_list     = data[1]
    lettre_list   = data[2]

    length = len(lettre_list)
    chaine = ""
    k,i = 0,0
    
    while i < length : 
        
        New_chaine =""

        if position_list[i] == 0 and size_list[i] == 0 :
            chaine += lettre_list[i]
            
            k+=1
            ShowNormalDecryptSteps(k,chaine,lettre_list[i])  
        
        else :
            position = len(chaine)-position_list[i]-1
            New_chaine =  chaine[position:position+size_list[i]]
            
            k+=1

            chaine += New_chaine
            chaine+= lettre_list[i]
            ShowRedundancyDecryptSteps(k,chaine,position_list[i],size_list[i],lettre_list[i])


        i+=1
    
    PrintStatement(Statement)

    if chaine == Statement :
        print("\n *** It's Done !!! ***\n")
