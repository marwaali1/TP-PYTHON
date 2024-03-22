def poids(s):
    s = s.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    voy = "AEIOUY"
    pos = 1
    poids = 0
    for Lettre in s:
        if Lettre in voy:
            poids += pos*(alpha.find(Lettre)+1)
        pos += 1
 
    return poids
 
 
print(poids("BONNE"))
print(poids("CHANCE"))