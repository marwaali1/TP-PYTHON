def chiffre_cesar(message, decalage):
    message_chiffre = ''
    for caractere in message:
        if caractere.isalpha():
            minuscule = caractere.islower()
            ascii_offset = ord('a') if minuscule else ord('A')
            nouveau_caractere = chr((ord(caractere) - ascii_offset + decalage) % 26 + ascii_offset)
            message_chiffre += nouveau_caractere
        else:
            message_chiffre += caractere
    return message_chiffre
message_entree = input("Entrez un message : ")
decalage_entree = int(input("Entrez le décalage souhaité : "))
message_chiffre = chiffre_cesar(message_entree, decalage_entree)
print("Message chiffré :", message_chiffre)
