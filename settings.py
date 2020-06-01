SIZE = (WIDTH, HEIGHT) = (650, 650)
WHITE = (155, 155, 255)
DETIME = 3000
BLASTIME = 1000
WALLSIZE = 50
AISLEENTERS = 5# defines a spreed of help on turns
#WEAPONS = [Dynamite]


lines = [25 + 100*i for i in range(0, 7)]

explines = []
for i in lines:
    for j in range(- AISLEENTERS, AISLEENTERS + 1):
        explines.append(i + j)