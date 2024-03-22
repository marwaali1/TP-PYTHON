personnes = {
    'marwa': {'age': 32, 'ville': 'fes'},
    'sara': {'age': 30, 'ville': 'New York'},
    'hajar': {'age': 22, 'ville': 'casa'}
}

personnes['mari'] = {'age': 28, 'ville': 'meknes'}

print("Informations des personnes :")
for nom, infos in personnes.items():
    print(f"Nom: {nom}, age: {infos['age']}, Ville: {infos['ville']}")

villes = [infos['ville'] for infos in personnes.values()]

print("\nVilles d'origine :")
for ville in villes:
    print(ville)

villes.sort()
print("\nVilles triées par ordre alphabétique :", villes)

print("\nNombre d'occurrences de chaque ville :")
for ville in set(villes):
    print(f"{ville}: {villes.count(ville)} fois")

print("\nNom et âge de chaque personne :")
for nom, infos in personnes.items():
    print(f"{nom}: {infos['age']} ans")

premiere_personne = personnes.popitem()
print(f"\nPersonne supprimée : {premiere_personne}")
print("Nouvelles informations des personnes après suppression :")
for nom, infos in personnes.items():
    print(f"Nom: {nom}, age: {infos['age']}, Ville: {infos['ville']}")
