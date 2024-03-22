def premier(n):
    if n == 2:
        return True
    etat = True
    for i in range(2,int(n/2)):
        if n % i == 0:
            etat = False
            break
    return etat

def circulaire(n):
    n=str(n)
    for i in range (len(n)):
        if not premier(int(n)):
            return False
        n = n[1:] +n[0]
        return True
print(circulaire(719))



