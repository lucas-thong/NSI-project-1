# Module par sebastien chanthery

import turtle
from trait import trait

# ----- Sol de la rue -----
def sol(y_sol):
    turtle.pensize(3)
    turtle.pencolor(200,200,200)
    turtle.penup()
    turtle.setpostition(-405,y_sol)
    turtle.pendown()
    turtle.setposition(405,y_sol)


    '''
    Paramètres
        y_sol : ordonnée du sol du la rue
    Cete fonction dessine un trait horizontale de 3 pixels d'épaisseur
    '''

    pass


if __name__ == '__main__':
    sol(0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()