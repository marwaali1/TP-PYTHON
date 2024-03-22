
for c in range(1, 10):
    for d in range(10):
        for u in range(10): 
            som=c+d+u
            prod=c*d*u
            num=100*c+10*d+u
        if som!=0 & prod % som==0:
            print(num)
