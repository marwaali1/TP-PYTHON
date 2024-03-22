password= "hhhh1234"
def NbCMin(password):
    c = 0
    for i in password:
        if i.islower():
            c = c+1
    return c


def NbCMaj(password):
    c = 0
    for char in password:
        if char.isupper():
            c = c+ 1
    return c


def NbCAlphapass(password):
    c = 0
    for char in password:
        if not char.isalpha():
            c = c +  1
    return c


def LongMaj(password):
    max_sc = 0
    current_sc = 0

    for char in password:
        if char.isupper():
            current_sc= current_sc + 1
            max_sc = max(max_sc, current_sc)
        else:
            current_sc = 0
    return max_sc


def LongMin(password):
    max_sc = 0
    current_sc = 0

    for char in password:
        if char.islower():
            current_sc = current_sc + 1
            
            max_sc= max(max_sc, current_sc)
        else:
            current_sc = 0

    return max_sc

def score(password):
    bonus = (len(password)-NbCMin(password))*3+(len(password) -NbCMaj(password))*2+(len(password)-NbCAlphapass(password))*5
    penalites = LongMaj(password)*3+LongMin(password)*2
    val = bonus-penalites
    if val < 20:
        print('Très faible')
    elif val < 40:
        print('Faible')
    elif val < 80:
        print('Fort')
    else:
        print('Très fort')


print(score(password))



