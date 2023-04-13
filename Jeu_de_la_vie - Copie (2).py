from tkinter import *
from random import randint



jeu= Tk() #création d'une fénêtre
jeu.title("Jeu de la vie")
canvas = Canvas(jeu, width=300, height=200) #une fenêtre de type Canvas
canvas.pack()



def carres():
    #définition des carrés de manière aléatoire

        #carré A

    remplissagenb=randint(0,1)

    if remplissagenb==0:
        remplissage="white"


    elif remplissagenb==1:
        remplissage="black"

    global remplissageA
    remplissageA=remplissage

    global A
    A = canvas.create_rectangle((0, 0, 20, 20), outline="gray", fill=remplissageA)




        #carré B

    remplissagenb=randint(0,1)
    if remplissagenb==0:
        remplissage="white"


    elif remplissagenb==1:
        remplissage="black"

    global remplissageB
    remplissageB=remplissage

    global B
    B = canvas.create_rectangle((20, 0, 40, 20), outline="gray", fill=remplissageB)


        #carré C
    remplissagenb=randint(0,1)
    if remplissagenb==0:
        remplissage="white"


    elif remplissagenb==1:
        remplissage="black"


    global remplissageC
    remplissageC=remplissage

    global C
    C = canvas.create_rectangle((40, 0, 60, 20), outline="gray", fill=remplissageC)


        #carré D
    remplissagenb=randint(0,1)
    if remplissagenb==0:
        remplissage="white"

    elif remplissagenb==1:
        remplissage="black"

    global remplissageD
    remplissageD=remplissage

    global D
    D = canvas.create_rectangle((0, 20, 20, 40), outline="gray", fill=remplissageD)



        #carré E
    remplissagenb=randint(0,1)
    if remplissagenb==0:
        remplissage="white"


    elif remplissagenb==1:
        remplissage="black"

    global remplissageE
    remplissageE=remplissage

    global E
    E = canvas.create_rectangle((20, 20, 40, 40), outline="gray", fill=remplissageE)


        #carré F
    remplissagenb=randint(0,1)
    if remplissagenb==0:
        remplissage="white"

    elif remplissagenb==1:
        remplissage="black"


    global remplissageF
    remplissageF=remplissage

    global F
    F = canvas.create_rectangle((40, 20, 60, 40), outline="gray", fill=remplissageF)


        #carré G
    remplissagenb=randint(0,1)
    if remplissagenb==0:
        remplissage="white"


    elif remplissagenb==1:
        remplissage="black"


    global remplissageG
    remplissageG=remplissage

    global G
    G = canvas.create_rectangle((0, 40, 20, 60), outline="gray", fill=remplissageG)


        #carré H
    remplissagenb=randint(0,1)
    if remplissagenb==0:
        remplissage="white"


    elif remplissagenb==1:
        remplissage="black"


    global remplissageH
    remplissageH=remplissage

    global H
    H = canvas.create_rectangle((20, 40, 40, 60), outline="gray", fill=remplissageH)


        #carré I
    remplissagenb=randint(0,1)
    if remplissagenb==0:
        remplissage="white"


    elif remplissagenb==1:
        remplissage="black"


    global remplissageI
    remplissageI=remplissage

    global I
    I = canvas.create_rectangle((40, 40, 60, 60), outline="gray", fill=remplissageI)





#applications des règles



def regles():

    global remplissageA
    global remplissageB
    global remplissageC
    global remplissageD
    global remplissageE
    global remplissageF
    global remplissageG
    global remplissageH
    global remplissageI



    #on actualise la fenêtre
    canvas.itemconfig(A, fill=remplissageA)
    canvas.itemconfig(B, fill=remplissageB)
    canvas.itemconfig(C, fill=remplissageC)
    canvas.itemconfig(D, fill=remplissageD)
    canvas.itemconfig(E, fill=remplissageE)
    canvas.itemconfig(F, fill=remplissageF)
    canvas.itemconfig(G, fill=remplissageG)
    canvas.itemconfig(H, fill=remplissageH)
    canvas.itemconfig(I, fill=remplissageI)


    countA=0
    countB=0
    countC=0
    countD=0
    countE=0
    countF=0
    countG=0
    countH=0
    countI=0

        #compte des voisins


        #de A
    if remplissageB=="black":
        countA=countA+1
    if remplissageD=="black":
        countA=countA+1
    if remplissageE=="black":
        countA=countA+1

    #de B
    if remplissageA=="black":
        countB=countB+1
    if remplissageD=="black":
        countB=countB+1
    if remplissageE=="black":
        countB=countB+1
    if remplissageF=="black":
        countB=countB+1
    if remplissageC=="black":
        countB=countB+1


    #de C
    if remplissageB=="black":
        countC=countC+1
    if remplissageF=="black":
        countC=countC+1
    if remplissageE=="black":
        countC=countC+1


    #de D
    if remplissageB=="black":
        countD=countD+1
    if remplissageA=="black":
        countD=countD+1
    if remplissageE=="black":
        countD=countD+1
    if remplissageG=="black":
        countD=countD+1
    if remplissageH=="black":
        countD=countD+1

    #de E
    if remplissageA=="black":
        countE=countE+1
    if remplissageB=="black":
        countE=countE+1
    if remplissageC=="black":
        countE=countE+1
    if remplissageD=="black":
        countE=countE+1
    if remplissageF=="black":
        countE=countE+1
    if remplissageG=="black":
        countE=countE+1
    if remplissageH=="black":
        countE=countE+1
    if remplissageI=="black":
        countE=countE+1

    #de F
    if remplissageB=="black":
        countF=countF+1
    if remplissageC=="black":
        countF=countF+1
    if remplissageE=="black":
        countF=countF+1
    if remplissageH=="black":
        countF=countF+1
    if remplissageI=="black":
        countF=countF+1

    #de G
    if remplissageH=="black":
        countG=countG+1
    if remplissageD=="black":
        countG=countG+1
    if remplissageE=="black":
        countG=countG+1

    #de H
    if remplissageF=="black":
        countH=countH+1
    if remplissageD=="black":
        countH=countH+1
    if remplissageE=="black":
        countH=countH+1
    if remplissageG=="black":
        countH=countH+1
    if remplissageI=="black":
        countH=countH+1

    #de I
    if remplissageF=="black":
        countI=countI+1
    if remplissageE=="black":
        countI=countI+1
    if remplissageH=="black":
        countI=countI+1



        #on change la couleur des carrés si besoin

        # pour A
    if remplissageA=="white":
        if countA==3:
            remplissageA="black"

    elif remplissageA=="black":
        if countA<2:
            remplissageA="white"
        if countA>3:
            remplissageA="white"

    # pour B
    if remplissageB=="white":
        if countB==3:
            remplissageB="black"

    elif remplissageB=="black":
        if countB<2:
            remplissageB="white"
        if countB>3:
            remplissageB="white"


    # pour C
    if remplissageC=="white":
        if countC==3:
            remplissageC="black"

    elif remplissageC=="black":
        if countC<2:
            remplissageC="white"
        if countC>3:
            remplissageC="white"

    # pour D
    if remplissageD=="white":
        if countD==3:
            remplissageD="black"

    elif remplissageD=="black":
        if countD<2:
            remplissageD="white"
        if countD>3:
            remplissageD="white"

    # pour E
    if remplissageE=="white":
        if countE==3:
            remplissageE="black"

    elif remplissageE=="black":
        if countE<2:
            remplissageE="white"
        if countE>3:
            remplissageE="white"

    # pour F
    if remplissageF=="white":
        if countF==3:
            remplissageF="black"

    elif remplissageF=="black":
        if countF<2:
            remplissageF="white"
        if countF>3:
            remplissageF="white"


    # pour G
    if remplissageG=="white":
        if countG==3:
            remplissageG="black"

    elif remplissageG=="black":
        if countG<2:
            remplissageG="white"
        if countG>3:
            remplissageG="white"

    # pour H
    if remplissageH=="white":
        if countH==3:
            remplissageH="black"

    elif remplissageH=="black":
        if countH<2:
            remplissageH="white"
        if countH>3:
            remplissageH="white"

    # pour I
    if remplissageI=="white":
        if countI==3:
            remplissageI="black"

    elif remplissageI=="black":
        if countI<2:
            remplissageI="white"
        if countI>3:
            remplissageI="white"



    jeu.after(1000,regles)



carres()
regles()
jeu.mainloop()



