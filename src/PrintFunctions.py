
def ShowRedundancySteps(k,gauche,droite,position=0,chaine="",lettre=""):
    
    length = str(len(chaine))
    print(" {}. gauche = \" {} \" , droite = \" {}\" : code < {},{},'{}'>".format(k,gauche,droite,position,length,lettre))

def ShowNormalSteps(k,gauche,droite,lettre=""):

    print(" {}. gauche = \" {} \" , droite = \" {}\" : code < 0,0,'{}'>".format(k,gauche,droite,lettre))


def ShowRedundancyDecryptSteps(k,chaine,position,size,lettre=""):
    
    print(" {}. {}  : code < {},{},'{}'>".format(k,chaine,position,size,lettre))


def ShowNormalDecryptSteps(k,chaine,lettre) :
    print(" {}. {}  : code < 0,0,'{}'>".format(k,chaine,lettre))


def PrintStatement(Statement):
    print("\n Statement :  {} \n".format(Statement))

