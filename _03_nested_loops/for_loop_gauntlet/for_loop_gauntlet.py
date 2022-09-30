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
    pass
