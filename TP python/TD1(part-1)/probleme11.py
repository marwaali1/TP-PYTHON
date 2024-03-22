password= "idsd2004hhhHHHclass"
def NbCMin(password):
    return sum([1 for i in password if i.islower()])
print(NbCMin(password))



def NbCMaj(password):
    return sum([1 for i in password if i.islower()])
print(NbCMin(password))



def NbCAlphapass(password):
    return sum([ 1 for i in password if not i.isalpha()])
print(NbCAlphapass(password))




print(NbCMin(password))

print(NbCMaj(password))

print(NbCAlphapass(password))






