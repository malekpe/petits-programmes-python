#choix programme
print("1 = nombre pair ou impair")
print("2 = calcul prix soldé")
print("3 = conteur automatique")
print("4 = donne table de multiplication")
print("5 = calcul le carré d'un nombre")
print("6 = calcul solution équation second degré")
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
