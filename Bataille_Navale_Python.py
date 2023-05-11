import random

ligne=[]
for i in range (0,10):
    ligne.append([0,0,0,0,0,0,0,0,0,0])

for l in ligne:
    print(l)



nbr=int(input("nbr navires ?"))
a=0
while (a<nbr):
    nbr_x=(random.randint(0,9))
    nbr_y=(random.randint(0,9))
    if ligne [nbr_x] [nbr_y] !=1 :
        ligne [nbr_x] [nbr_y]=1
        a+=1
    

for l in ligne:
    print(l)


