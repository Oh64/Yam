import turtle as tortue

def tortue_reset():
    tortue.reset()
    tortue.clear()
    tortue.home()
    tortue.hideturtle()
    tortue.speed(0)
    tortue.up()
    tortue.goto(-300, 200)
    tortue.tracer(0) # Stop Python !! N'acctualise pas la fenetre

def carre():
    for i in range(4):
        tortue.down()
        tortue.forward(100)
        tortue.right(90)
        tortue.up()

def de1():
    tortue.forward(50)
    tortue.right(90)
    tortue.forward(50)
    tortue.dot(25)
    tortue.right(180)
    tortue.forward(50)
    tortue.left(90)
    tortue.forward(50)
    tortue.right(180)


def de2():
    tortue.forward(75)
    tortue.right(90)
    tortue.forward(25)
    tortue.dot(25)
    tortue.forward(50)
    tortue.right(90)
    tortue.forward(50)
    tortue.dot(25)
    tortue.forward(25)
    tortue.right(90)
    tortue.forward(75)
    tortue.right(90)


def de3():
    tortue.forward(75)
    tortue.right(90)
    tortue.forward(25)
    tortue.down()
    tortue.dot(25)
    tortue.up()
    tortue.forward(50)
    tortue.right(90)
    tortue.forward(50)
    tortue.dot(25)
    tortue.right(180)
    tortue.forward(25)
    tortue.left(90)
    tortue.forward(25)
    tortue.dot(25)
    tortue.forward(50)
    tortue.left(90)
    tortue.forward(50)
    tortue.right(180)


def de4():
    tortue.forward(75)
    tortue.right(90)
    tortue.forward(25)
    tortue.dot(25)
    tortue.forward(50)
    tortue.dot(25)
    for i in range(2):
        tortue.right(90)
        tortue.forward(50)
        tortue.dot(25)
    tortue.forward(25)
    tortue.left(90)
    tortue.forward(25)
    tortue.right(180)


def de5():
    tortue.forward(75)
    tortue.right(90)
    tortue.forward(25)
    tortue.dot(25)
    tortue.forward(50)
    tortue.dot(25)
    for i in range(2):
        tortue.right(90)
        tortue.forward(50)
        tortue.dot(25)
    for i in range(2):
        tortue.right(90)
        tortue.forward(25)
    tortue.dot(25)
    tortue.right(180)
    tortue.forward(50)
    tortue.left(90)
    tortue.forward(50)
    tortue.right(180)


def de6():
    tortue.forward(75)
    tortue.right(90)
    tortue.forward(20)
    for i in range(2):
        tortue.dot(25)
        tortue.forward(30)
    tortue.dot(25)
    tortue.right(90)
    tortue.forward(50)
    tortue.right(90)
    for i in range(2):
        tortue.dot(25)
        tortue.forward(30)
    tortue.dot(25)
    tortue.forward(20)
    tortue.left(90)
    tortue.forward(25)
    tortue.right(180)


def avance():
    tortue.forward(125)

# écriture du numéro du dès
def nombre_de(nbr):
    tortue.up()
    tortue.left(90)
    tortue.forward(10)
    tortue.write(f"Dé {nbr}", font=("Arial", 20,'normal'))
    tortue.left(180)
    tortue.forward(10)
    tortue.left(90)

def resultat_trace(nd):
    if nd == 1:
        de1()
    if nd == 2:
        de2()
    if nd == 3:
        de3()
    if nd == 4:
        de4()
    if nd == 5:
        de5()
    if nd == 6:
        de6()


def drawdes(des):
    #if reset:
        #tortue_reset()
        #tortue_reset()
    tortue_reset()

    carre()
    nombre_de(1)
    resultat_trace(des[0])
    avance()
    carre()
    nombre_de(2)
    resultat_trace(des[1])
    avance()
    carre()
    nombre_de(3)
    resultat_trace(des[2])

    tortue.right(90)
    tortue.forward(170)
    tortue.right(90)
    tortue.forward(62.5)
    tortue.right(180)

    carre()
    nombre_de(5)
    resultat_trace(des[4])
    tortue.right(180)
    tortue.forward(125)
    tortue.right(180)
    carre()
    nombre_de(4)
    resultat_trace(des[3])
    tortue.update()
