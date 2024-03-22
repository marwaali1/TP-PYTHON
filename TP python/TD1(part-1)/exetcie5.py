def premier(n):
    if n == 2:
        return True
    etat = True
    for i in range(2,int(n/2)):
        if n % i == 0:
            etat = False
            break
    return etat
 
def circulaire(p, q):
    for i in range(p, q+1):
        if premier(i) == True:
            etat = True
            c = str( i)
            k = 0
            while k < len(c) and etat == True:
                c = c[-1]+c[:len(c)-1]
                if premier(int(c)) == False:
                    etat = False
                    break
                k += 1
            if etat == True:
                print(' le nombre : ', i)

circulaire(10,100)




 
