from pygame import *
from random import randint


init()
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180,0,0))

                                                                                                  
h = 700
w = 500
window = display.set_mode((h, w))
display.set_caption("Пон")
backround = transform.scale(image.load("galaxy.jpg"), (h, w))
game = True
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, s, x, y, w, h):
        super().__init__()
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(player_image), (self.w,self.h))
        self.speed = s
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
       
class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 645:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 645:
            self.rect.y += self.speed
ball = GameSprite("ufo.png", 5, 350, 300, 70,70)

player1 = Player("rocket.png", 5, 20, 300, 70,70)
player2 = Player("rocket.png", 5, 600, 300, 70,70)
speed_y =2
speed_x =4
finish = True
while game:
    keys_pressed = key.get_pressed()
    clock.tick(60)
    window.blit(backround, (0,0))
    player1.reset()
    player1.update1()
    player2.reset()
    player2.update2()
    ball.reset()
    for a in event.get():
        if a.type == QUIT:
            game = False
    if finish == True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > w-50 or ball.rect.y < 0:
            speed_y *= -1

        

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (250, 250))
            game_over = True

        if ball.rect.x > h:
            finish = True
            window.blit(lose2, (250, 250))
            game_over = True
    display.update()