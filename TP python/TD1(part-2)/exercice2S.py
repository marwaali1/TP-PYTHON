def crypter_mot(mot):
    mot_crypte = ''
    for lettre in mot.upper():
        if lettre.isalpha():
            n = mot.count(lettre)
            k = 2 * n if n % 2 != 0 else n // 2
            lettre_crypte = chr((ord(lettre) - 65 + k) % 26 + 65)
            mot_crypte += lettre_crypte
        else:
            mot_crypte += lettre
    return mot_crypte
mot_entree = input("Entrez un mot (composé uniquement de lettres majuscule):")
print("Mot crypté :", crypter_mot(mot_entree))
