import pygame
import time
import math
import random

screen_width = 600
screen_height = 400

pygame.init()
window = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont('Tohama', 40, True, False)

# classes


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 50
        self.h = 80
        self.speed = 15
        self.points = 0

        self.left = False
        self.rigth = False
        self.time = True

    def setLeft(self, mode):
        self.left = mode

    def setRigth(self, mode):
        self.rigth = mode

    def setTime(self, mode):
        self.time = mode

    def update(self):
        if (self.left):
            if (self.x > 0):
                self.x -= self.speed
            else:
                self.x = 0
        elif (self.rigth):
            if (self.x < 550):
                self.x += self.speed
            else:
                self.x = 550

    def render(self, window):
        pygame.draw.rect(window, (160, 32, 240), pygame.Rect(
            self.x, self.y, self.w, self.h))


class Ball():
    def __init__(self, x, y, a, b, c, dy):
        self.x = x
        self.y = y
        self.init_x = x
        self.init_y = y
        self.r = 15
        self.dx = 0
        self.dy = dy
        self.color = (a, b, c)

    def reset(self):
        self.y = self.init_y
        self.x = random.randint(15, screen_width - 15)

    def update(self):
        if (self.y + self.r) >= screen_height or (self.y) <= 0:
            self.dy *= 1
        self.x += self.dx
        self.y += self.dy

    def render(self, window):
        pygame.draw.ellipse(window, (self.color), pygame.Rect(
            self.x, self.y, self.r, self.r))


# variables
player_1 = Player(250, 300)
ball_blue = Ball(screen_width // 2, 5, 0, 255, 0, 8)
ball_red = Ball(screen_width // 3, 5, 255, 0, 0, 5)

running = True

while (running):
    pygame.draw.rect(window, (255, 255, 255), pygame.Rect(
        0, 0, screen_width, screen_height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_1.setRigth(True)
            if event.key == pygame.K_LEFT:
                player_1.setLeft(True)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_1.setRigth(False)
            if event.key == pygame.K_LEFT:
                player_1.setLeft(False)

    player_1.update()
    ball_blue.update()
    ball_red.update()

    ball_rect1 = pygame.Rect(ball_blue.x, ball_blue.y,
                             ball_blue.r, ball_blue.r)
    ball_rect2 = pygame.Rect(ball_red.x, ball_red.y, ball_red.r, ball_red.r)
    player1_rect = pygame.Rect(player_1.x, player_1.y, player_1.w, player_1.h)

    if (ball_rect1.colliderect(player1_rect)):
        player_1.points += 1
        ball_blue.reset()

    if (ball_rect2.colliderect(player1_rect)):
        player_1.points -= 1
        ball_red.reset()

    if (ball_blue.y > screen_height):
        ball_blue.reset()
        player_1.points -= 1

    if (ball_red.y > screen_height):
        ball_red.reset()

    pontos_p1 = font.render(str(player_1.points), False, (0, 0, 0))
    window.blit(pontos_p1, (10, 20))

    player_1.render(window)
    ball_blue.render(window)
    ball_red.render(window)

    pygame.display.update()
    time.sleep(0.05)
