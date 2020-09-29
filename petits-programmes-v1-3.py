while(0==0):
    print("")
    #choix programme
    print("1 = nombre pair ou impair")
    print("2 = calcul prix soldé")
    print("3 = conteur automatique")
    print("4 = donne table de multiplication")
    print("5 = calcul le carré d'un nombre")
    print("6 = calcul solution équation second degré")
    print("7 = multi-convertisseur binaire décimal hexadecimal")
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
