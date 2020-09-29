def decbin(base10):
    resultat=str("")
    while(base10>=1):
        reste=base10%2
        base10=int(base10/2)
        resultat=str(reste)+str(resultat)

    return(resultat)


def bindec(binaire):
    resultat=int(0)
    exposant=0
    trad=binaire
    while(trad>=1):
        reste=trad%2
        trad=int(trad/10)
        chiffre=reste
        resultat=int(chiffre*2**exposant)+int(resultat)
        exposant+=1

    return(resultat)

def dechexa(base10):
    resultat=str("")
    while(base10>=1):
        reste=base10%16
        convers="123456789ABCDEF"
        incconv=0
        while (incconv<16):
            if (reste==incconv+1):
                reste=str(convers[incconv])

            incconv+=1
        base10=int(base10/16)
        resultat=str(reste)+str(resultat)

    return(resultat)

def hexadec(hexa):
    resultat=0
    exposant=0
    trad=hexa
    lettre=int(len(hexa))-1
    while(lettre!=-1):
        chiffre=trad[lettre]
        convers="123456789ABCDEF"
        incconv=0
        while (type(chiffre)!=type(1)):
            if (chiffre==convers[incconv]):
                chiffre=incconv+1

            incconv+=1
        resultat=int(chiffre*16**exposant)+int(resultat)
        exposant+=1
        lettre-=1

    return(resultat)

def binc2dec(binc2):
    binaire=int(binc2)
    resultat=int(0)
    exposant=0
    trad=binaire
    while(trad>=1):
        reste=trad%2
        trad=int(trad/10)
        chiffre=reste
        resultat=int(chiffre*2**exposant)+int(resultat)
        exposant+=1
    if(binc2[0]=="1"):
        puissance=int(len(str(binaire)))
        resultat=resultat-2**puissance

    return(resultat)

while(0==0):
    print("1 = Ton nombre est en binaire")
    print("2 = Ton nombre est en décimal")
    print("3 = Ton nombre est en hexadécimal")
    print("4 = Ton nombre est en binaire(c2)")
    choix=input("Choisix parmis les propositions ci-dessus : ")
    lenombre=input("mets ton nombre : ")
    print("")
    if (choix=="1"):
        print("ton nombre en binaire : ", lenombre)
        print("ton nombre en décimal : ", bindec(int(lenombre)))
        print("ton nombre en hexadécimal : ", dechexa(bindec(int(lenombre))))
    if (choix=="2"):
        print("ton nombre en binaire : ", decbin(int(lenombre)))
        print("ton nombre en décimal : ", lenombre)
        print("ton nombre en hexadécimal : ", dechexa(int(lenombre)))
    if (choix=="3"):
        print("ton nombre en binaire : ", decbin(int(hexadec(lenombre))))
        print("ton nombre en décimal : ", hexadec(lenombre))
        print("ton nombre en hexadécimal : ", lenombre)
    if (choix=="4"):
        print("ton nombre en binaire(c2) : ", lenombre)
        print("ton nombre en décimal : ", binc2dec(str(lenombre)))
    print("")
    print("")
