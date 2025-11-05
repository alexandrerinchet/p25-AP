"""
v04 : on crée le serpent
"""
from random import randint
import pygame as pg

def damier() :
    x, y = 0, 0
    width, height = 20, 20
    color = (255, 255, 255)     
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

def serpent_fixe(snake):
    for coord in snake :
        x, y = coord
        #on convertit la position en bloc en position en pixels (chaque bloc faisant 20pixels de longueur/largeur)
        rect = pg.Rect(x*20, y*20, 20, 20) 
        pg.draw.rect(screen, (0, 255, 0), rect)
    return

def serpent_bouge(snake, dir):
    x,y=snake[-1]
    dirx, diry = dir
    nouv=(x+dirx,y+diry)
    snake.pop(0)
    snake.append(nouv)
    return snake

def dessin_fruit(fruit):
    x, y = fruit
    rect = pg.Rect(x*20, y*20, 20, 20)
    pg.draw.rect(screen, (255, 0, 0), rect)
    return

def mange_fruit(snake, fruit, score):
    if snake[-1] == fruit :
        fruit = (randint(0, 29), randint(0, 29))
        snake.insert(0, snake[0])
        score += 1
    return snake, fruit, score
    

def perdu(snake):
    if snake[-1] in snake[:len(snake)-1]:
        return True
    return False


# les coordonnées du corps du serpent
snake = [
    (10, 15),
    (11, 15),
    (12, 15),
]

dir =(1,0)

fruit = (randint(0,29),randint(0,29))

score = 0

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:

    clock.tick(5)

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
            elif event.key == pg.K_UP:
                dir = (0, -1)
            elif event.key == pg.K_DOWN:
                dir = (0, 1)
            elif event.key == pg.K_LEFT:
                dir = (-1, 0)
            elif event.key == pg.K_RIGHT:
                dir = (1, 0)

    # xxx ici c'est discutable, car si on tape 'q'
    # on va quand même changer de couleur avant de sortir...
    screen.fill((0, 0, 0))
    damier()
    snake = serpent_bouge(snake, dir)
    snake, fruit, score = mange_fruit(snake, fruit, score)
    serpent_fixe(snake)
    dessin_fruit(fruit)
    if perdu(snake):
        running = False
    pg.display.update()
    pg.display.set_caption(f"Score: {score}")

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()
