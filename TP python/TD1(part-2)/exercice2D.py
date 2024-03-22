def echange_cles_valeurs(dictionnaire):
    dictionnaire_inverse = {v: k for k, v in dictionnaire.items()}
    return dictionnaire_inverse
dictionnaire_original = {'apple': 'pomme', 'banana': 'banane', 'orange': 'orange'}
dictionnaire_inverse = echange_cles_valeurs(dictionnaire_original)
print("Dictionnaire original :", dictionnaire_original)
print("Dictionnaire inversé :", dictionnaire_inverse)
