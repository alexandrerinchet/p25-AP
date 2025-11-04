"""
v03 : on crée le damier
"""
def damier() :
    x, y = 0, 0
    width, height = 20, 20
    color = (255, 0, 0)     
    for i in range(30):
        for _ in range(15):
            rect = pg.Rect(x, y, width, height)
            pg.draw.rect(screen, color, rect)
            y += 40
        x += 20
        if i % 2 == 0:
            y = 20
        else:
            y = 0
    return

from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((400, 300))
clock = pg.time.Clock()

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:

    clock.tick(1)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False

    # xxx ici c'est discutable, car si on tape 'q'
    # on va quand même changer de couleur avant de sortir...

    damier()
    pg.display.update()


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()
