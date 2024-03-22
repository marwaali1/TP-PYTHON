num = int(input("Entrez un entier naturel positif : "))

for i in range(1, num):
    if i+ sum(map(int, str(i))) == num:
        print(num, "n'est pas un auto-nombre.")
        break
else:
    print(num, "n'est pas un auto-nombre.")