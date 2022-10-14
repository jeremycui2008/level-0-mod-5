"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':

    for z in range (101):
        z=-z+100
        print(z)
    for ix in range (100):
        ix=ix
        print(ix)

    for i in range (51):
        if i>0:
            i=i*2
            print(i)
    for zy in range (101):
        if zy%2==0:
            print()
        else:
            print(zy)
    for l in range (501):
        if l%2==0:
            print(str(l) +'is an even number')
        else:
            print(str(l)+'is an odd number')
    for t in range (112):
        t=t*7
        print(t)
    year=2022
    for guh in range(14):
        if guh==1:
            year-=13
            print("In " + str(year) + " I was " + str(guh) + " years old")
        if guh>1:
            year+=1
            print("In " + str(year) + " I was " + str(guh) + " years old")
    for gu in range(3):

        for g in range(3):

            print(str(gu) + ''+  str(g))
    for xy in range(3):
        if xy>=1:
            print('')
        for xyz in range(3):
            w = xy+xy+xy+xyz+1
            print(w, end=" ")
    print('')
    for die in range(10):
        if die>=1:
            print('')
        for dies in range(10):
            dice = die+die+die+die+die+die+die+die+die+die+dies+1
            print(dice, end=" ")
    print('')
    bruh=''
    for kill in range(6):
        bruh+='*'
        print(bruh)
    pass
