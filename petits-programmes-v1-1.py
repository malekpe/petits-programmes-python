#choix programme
print("1 = nombre pair ou impair")
print("2 = calcul prix soldé")
print("3 = conteur automatique")
print("4 = donne table de multiplication")
print("5 = calcul le carré d'un nombre")
print("6 = calcul solution équation second degré")
print("7 = traduis base10 vers binaire")
print("8 = traduis base10 vers hexadécimal")
print("9 = traduis binaire vers base10")
choix=int(input("choisis le programme que tu veux grâce a son numéro : "))

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
    base10=int(input("mets un nombre que tu veux traduire en binaire : "))
    resultat=str("")
    while(base10>=1):
        reste=base10%2
        base10=int(base10/2)
        resultat=str(reste)+str(resultat)
    print(resultat)

if(choix==8):
    base10=int(input("mets un nombre que tu veux traduire en hexadécimal : "))
    resultat=str("")
    while(base10>=16):
        reste=base10%16
        if(reste==10):
            reste="A"
        if(reste==11):
            reste="B"
        if(reste==12):
            reste="C"
        if(reste==13):
            reste="D"
        if(reste==14):
            reste="E"
        if(reste==15):
            reste="F"
        base10=int(base10/16)
        resultat=str(reste)+str(resultat)
    reste=base10%16
    if(reste==10):
        reste="A"
    if(reste==11):
        reste="B"
    if(reste==12):
        reste="C"
    if(reste==13):
        reste="D"
    if(reste==14):
        reste="E"
    if(reste==15):
        reste="F"
    base10=int(base10/16)
    resultat=str(reste)+str(resultat)
    print(resultat)

if(choix==9):
    binaire=int(input("mets un nombre binaire que tu veux traduire en décimal : "))
    resultat=int(0)
    exposant=0
    trad=binaire
    while(trad>=1):
        reste=trad%2
        trad=int(trad/10)
        chiffre=reste
        resultat=int(chiffre*2**exposant)+int(resultat)
        exposant=exposant+1

    print(resultat)

if(choix==10):
    hexa=str(input("mets un nombre hexadécimal que tu veux traduire en décimal : "))
    resultat=int(0)
    exposant=0
    trad=hexa
    lettre=int(len(hexa))-1
    while(lettre!=-1):
        chiffre=trad[lettre]
        if(chiffre=="1"):
            chiffre=1
        if(chiffre=="2"):
            chiffre=2
        if(chiffre=="3"):
            chiffre=3
        if(chiffre=="4"):
            chiffre=4
        if(chiffre=="5"):
            chiffre=5
        if(chiffre=="6"):
            chiffre=6
        if(chiffre=="7"):
            chiffre=7
        if(chiffre=="8"):
            chiffre=8
        if(chiffre=="9"):
            chiffre=9
        if(chiffre=="A"):
            chiffre=10
        if(chiffre=="B"):
            chiffre=11
        if(chiffre=="C"):
            chiffre=12
        if(chiffre=="D"):
            chiffre=13
        if(chiffre=="E"):
            chiffre=14
        if(chiffre=="F"):
            chiffre=15
        resultat=int(chiffre*16**exposant)+int(resultat)
        exposant=exposant+1
        lettre=lettre-1

    print(resultat)
