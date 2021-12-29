
def ShowRedundancySteps(k,gauche,droite,position=0,chaine="",lettre=""):
    
    length = str(len(chaine))
    print(" {}. gauche = \" {} \" , droite = \" {}\" : code < {},{},'{}'>".format(k,gauche,droite,position,length,lettre))

def ShowNormalSteps(k,gauche,droite,lettre=""):

    print(" {}. gauche = \" {} \" , droite = \" {}\" : code < 0,0,'{}'>".format(k,gauche,droite,lettre))
