import pygame as pg
import math
from random import randint


WIDTH, HEIGHT = 900, 500
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snow")


BLUE = (13, 71, 161)
BROWN = (78, 52, 46)
WHITE = (255, 255, 255)

k = 0.000000004
m = 1e-7
dt = 0.05
alpha = math.radians(45)

class Particle:

    particles = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.particles.append(self)


    def create(n):
        for i in range(n):
            x = randint(-200, WIDTH)
            y = randint(200, 1000)
            new = Particle(x, -y)


    def update(self):
        if not self.fall():    
            G = m * 9.81
            L = k * math.sqrt(self.vx**2 + self.vy**2)
            Lx = L * math.sin(alpha)
            Ly = L * math.cos(alpha)

            ax = Lx / m
            ay = (G - Ly) / m

            self.vx += ax * dt
            self.x += self.vx * dt
            self.vy += ay * dt
            self.y += self.vy * dt

    
    def fall(self):
        if int(self.y) >= HEIGHT - 100:
            return True
        return False

    def draw(self):
        pg.draw.circle(WIN, WHITE, (self.x, self.y), 1)
    





def drawWin():
    GROUND = pg.Rect(0, HEIGHT - 100, WIDTH, 100)
    pg.draw.rect(WIN, BROWN, GROUND)
    pg.display.flip()



def main():
    clock = pg.time.Clock()

    particles = Particle.particles

    run = True
    while run:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        WIN.fill(BLUE)

        Particle.create(10)

        for particle in particles:
            particle.draw()
            particle.update()

        drawWin()
    

    pg.quit()


main()