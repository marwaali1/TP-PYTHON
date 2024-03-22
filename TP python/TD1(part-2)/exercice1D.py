def remplissage_dictionnaire():
    database = {}
    nb_copains = int(input("Entrez le nombre de copains à ajouter à la base de données : "))
    
    for _ in range(nb_copains):
        nom, age, taille = input("Entrez le nom, l'âge et la taille du copain (séparés par des espaces) : ").split()
        database[nom] = (int(age), float(taille))
    
    return database

def consultation_dictionnaire(database):
    while True:
        nom_recherche = input("Entrez le nom du copain à consulter (ou 'exit' pour quitter) : ").lower()
        
        if nom_recherche == 'exit':
            break
        
        copain = database.get(nom_recherche)
        if copain:
            print(f"Nom : {nom_recherche} - âge : {copain[0]} ans - taille : {copain[1]} m")
        else:
            print("Copain non trouvé dans la base de données.")

def main():
    base_de_donnees = remplissage_dictionnaire()
    consultation_dictionnaire(base_de_donnees)


