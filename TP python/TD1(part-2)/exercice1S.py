def crypter(ch):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for caractere in ch:
        indice = alpha.find(caractere)
        pos = indice+1
        if pos == 26:
            pos = 0
        res += alpha[pos]
    return res
print(crypter("ABDGET"))


