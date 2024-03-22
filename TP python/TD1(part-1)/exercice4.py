n = int(input("Entrez un entier n strictement positif et supérieur à 100 : "))
S = int((chiffre) for chiffre in str(n))
while S < 1 | S > 9:
    S = (int(chiffre) for chiffre in str(S))
code = int(str(S) + str(n))
print(f"Le code est :",code)


