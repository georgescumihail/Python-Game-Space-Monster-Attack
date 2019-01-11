import pygame
import random

pygame.init()

window = pygame.display.set_mode((800,600))
bck = pygame.image.load("media/background.jpeg")
paleta = pygame.image.load("media/paleta.png")
proiectil = pygame.image.load("media/proiectil.png")
monstru = pygame.image.load("media/monstru.png")
explozie = pygame.image.load("media/boom.png")
go = pygame.image.load("media/gameover.png")
muzica = pygame.mixer.music.load("media/sma-music.mp3")
font = pygame.font.SysFont('comicsans',30,True,False)

pygame.display.set_caption("Space Monster Attack")
pygame.mixer.music.play(-1)

x = 365
y = 570
speed = 8

class Projectile(object):
    def __init__(self, xcor, ycor, exists):
        self.xcor=xcor
        self.ycor=ycor
        self.exists=exists

class monster(object):
    def __init__ (self, xm, ym, alive):
        self.xm = xm
        self.ym = ym
        self.alive = alive


dead = False
run = True
shoot = False
clock = 0
difficulty = 1
enemies = []
score = 0

while run:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT]) and x > 5:
        x-=speed

    if (keys[pygame.K_RIGHT]) and x < 724:
        x+=speed

    if difficulty <= 7:
        difficulty += 0.0002

    clock += 1

    if (keys[pygame.K_SPACE]) and shoot == False:
        p1 = Projectile(x+28, y-45, True)
        shoot = True

    window.blit(bck,(0,0))
    window.blit(paleta,(x,y))

    text = font.render('Score: ' + str(score), 1, (250,250,250))
    window.blit(text,(20, 20))
    if shoot:
         if p1.exists == True:
             window.blit(proiectil, (p1.xcor, p1.ycor))
             p1.ycor -= 15
             if p1.ycor < 0:
                 p1.exists = False;
         else:
             shoot = False

    if clock * difficulty > 50:
         clock = 0
         rand = random.randint(0, 6)
         enemies.append(monster(rand * 100 + 150, 0, True))

    for e in enemies:
        if e.alive == True:
            window.blit(monstru,(e.xm,e.ym))
            e.ym += 3 * difficulty
        if shoot:
            if p1.ycor < e.ym + 15 and p1.xcor < e.xm + 40 and p1.xcor > e.xm - 20 and p1.exists == True and e.alive == True:
                if e.alive == True:
                    window.blit(explozie,(e.xm,e.ym))
                e.alive = False
                p1.exists = False
                score += 100
        if e.ym > 570:
            window.blit(go,(250, 230))
            dead = True
    pygame.display.update()
    if dead == True:
        pygame.time.delay(3000)
        run = False

print ("Your score was: ", score)