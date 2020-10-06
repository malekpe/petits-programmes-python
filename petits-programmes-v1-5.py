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
        convers="0123456789ABCDEF"
        incconv=0
        while (incconv<16):
            if (reste==incconv):
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
        convers="0123456789ABCDEFabcdef"
        incconv=0
        while (type(chiffre)!=type(1)):
            if (chiffre==convers[incconv]):
                chiffre=incconv
                if(chiffre==16 or chiffre==17 or chiffre==18 or chiffre==19 or chiffre==20 or chiffre==21):
                    chiffre=incconv-6
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

restart_all=True
while(restart_all==True):
    print("")
    #choix programme
    print("1 = nombre pair ou impair")
    print("2 = calcul prix soldé")
    print("3 = conteur automatique")
    print("4 = donne table de multiplication")
    print("5 = calcul le carré d'un nombre")
    print("6 = calcul solution équation second degré")
    print("7 = multi-convertisseur binaire décimal hexadecimal")
    print("8 = inverseur de texte")
    print("9 = mini jeu trouver un nombre")
    choix=int(input("choisis le programme que tu veux grâce a son numéro : "))
    print("")

    if(choix==1):#pair impair
        n=int(input("inséré un nombre : "))
        if n%2==0:
            print(n,"est pair")
        else:
            print(n,"est impair")

    if(choix==2):#prix soldé
        prix=float(input("choisis un prix en € : "))
        prix=prix-(prix*(float(input("choisis le montant de la réduction en % : "))/100))
        print("le prix soldé est égal à : ",prix,"€")

    if(choix==3):#conteur
        conter=int(input("tu veux conter jusqu'à combien ? "))
        jesuis=1
        while(jesuis<=conter):
            print(jesuis)
            jesuis=jesuis+1

    if(choix==4):#table de multiplication
        conter=int(input("tu veux quel table de multiplication : "))
        table=int(input("jusqu'à combien : "))
        jesuis=0
        while(jesuis<=table):
            print(conter,"x",jesuis,"=",jesuis*conter)
            jesuis=jesuis+1

    if(choix==5):#fonction
        def fonctiontropdeouf(n):
            print("bonsoir je suis la meilleur fonctioni de monde, tien",n,"au carré =",n*n)
        fonctiontropdeouf(int(input("un nombre que tu veux mettre au carré grace a la fonction trop de ouf")))

    if(choix==6):#équation second degré
        a=float(input("combien de x^2 ? : "))
        b=float(input("combien de x ? : "))
        c=float(input("quelle constante ? : "))
        delta=(b*b)-4*a*c
        print("delta est égal à : ", delta)
        if(delta<0):
            print("delta est négatif donc il n'y a pas de solution a l'équation dans R")
        if(delta>0):
            x1=((-b)+(delta**0.5))/(2*a)
            x2=((-b)-(delta**0.5))/(2*a)
            print("delta est positif donc l'équation à 2 solution : ", x1, " et ", x2)
        if(delta==0):
            x0=(-b)/(2*a)
            print("delta est égal à zéro donc l'équation a une unique solution : ", x0)

    if(choix==7):
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

    if(choix==8):#reverse caracteres
        chaine=input("entrer une chaine de caractères : ")
        resultat=""
        for i in range(len(chaine)):
            resultat=trad=chaine[i]+resultat
        print(resultat)

        texte=input("saisir du texte")
        for i in range(len(texte)-1,-1,-1):
            print(texte[i], end="")

    if(choix==9):
        from random import randint
        nombre=randint(1,100)
        nbtest=0
        jeu=False
        while(jeu!=True):
            nbtest+=1
            test=int(input("quel est le nombre ? : "))
            if(test==nombre):
                print("bravo tu a trouvé au bout de ", nbtest, " tentative !")
                jeu=True
            if(test<nombre):
                print("c'est plus !")
            if(test>nombre):
                print("c'est moins !")

    if(choix==10):
        print("entre une couleur sous la forme hexadécimal (exemple #F6A37B ou #F6B)")
        couleur=input("ou sous la forme décimal (exemple 235,45,123) : ")

        if(couleur[0]=="#" or couleur[0]=="$"):

            if(len(couleur)<5):#couvertie la forme supplifier d'un hexadecimal
                tradcouleur="#"
                for i in range(1,4,1):
                    doubleur=couleur[i]*2
                    tradcouleur+=doubleur
                couleur=tradcouleur

            resultat=""
            for i in range(1,7,2):
                conv_hexadec=couleur[i]+couleur[i+1]
                resultat+=str(hexadec(conv_hexadec))+","

            print("ta couleur sous forme décimal : ", resultat)

        if(couleur[0]!="#" and couleur[0]!="$"):

            couleur+=","
            if(couleur[1]==","):
                couleur="00"+couleur
            if(couleur[2]==","):
                couleur="0"+couleur
            if(couleur[5]==","):
                couleur=couleur[:4]+"00"+couleur[4:]
            if(couleur[6]==","):
                couleur=couleur[:4]+"0"+couleur[4:]
            if(couleur[9]==","):
                couleur=couleur[:8]+"00"+couleur[8:]
            if(couleur[10]==","):
                couleur=couleur[:8]+"0"+couleur[8:]

            resultat="#"
            for i in range(0,9,4):
                conv_dechexa=couleur[i]+couleur[i+1]+couleur[i+2]
                test=str(dechexa(int(conv_dechexa)))
                if(len(test)==1):
                    test="0"+test
                if(len(test)==0):
                    test="00"+test
                resultat+=test

            print("ta couleur sous forme hexadécimal : ", resultat)


    input("")
