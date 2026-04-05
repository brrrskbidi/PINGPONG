from pygame import *
from random import randint
window = display.set_mode((700,500))
display.set_caption('пинг-понг')
background67 = transform.scale(image.load('background.jpg'),(700,500))
futureback = transform.scale(image.load('futureback.jpg'),(700,500))
jungleback = transform.scale(image.load('jungleback.jpg'),(700,500))
scaryback = transform.scale(image.load('scaryback.jpg'),(700,500))

paused = False
clock = time.Clock()
font.init()
font1 = font.SysFont('Arial',36)
font2 = font.SysFont('Arial',60)
speed_h = 5
speed_w = 5


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,h,w):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(h,w))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP]and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[K_DOWN]and self.rect.y<430:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w]and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[K_s]and self.rect.y<430:
            self.rect.y += self.speed

rock1 = Player('rocket.jpg', 50,200,10,50,100)
rock2 = Player('rocket2.png',550,200,10,50,100)
defball = GameSprite('ball.png',200,200,10,50,50)
scaryball = GameSprite('scaryball.png',200,200,10,50,50)
jungleball = GameSprite('jungleball.png',200,200,10,50,50)
ball67 = GameSprite('ball67.png',200,200,10,50,50)
current_bg = background67
ball = defball
count1 = 0
count2 = 0
FPS = 60

game = True
finish = False
while game:
    window.blit(current_bg,(0,0))
    keys = key.get_pressed()
    if keys[K_1]:
        current_bg = futureback
    if keys[K_2]:
        current_bg = jungleback
        ball = jungleball
    if keys[K_3]:
        current_bg = background67
        ball = ball67
    if keys[K_4]:
        current_bg = scaryback
        ball = scaryball
    rock1.update_r()
    rock1.reset()
    rock2.update_l()
    rock2.reset()
    ball.reset() 
    counter = font1.render(str(count1)+':'+ str(count2), True, (255,255,255)) 
    window.blit(counter, (300,50))      
    if not paused:
        ball.rect.x+= speed_w
        ball.rect.y += speed_h
        if ball.rect.x >= 600:
            speed_w *= -1
        if ball.rect.y >= 400:
            speed_h *= -1
        if ball.rect.x <= 0:
            speed_w *= -1
        if ball.rect.y <=0:
            speed_h *= -1
        if sprite.collide_rect(ball,rock1):
            speed_w *=-1
        if sprite.collide_rect(ball,rock2):
            speed_w *=-1
        if  ball.rect.x< 80: 
            count2 +=1
            if current_bg == futureback:
                ball = GameSprite('ball.png',400,200,10,50,50)
            if current_bg == jungleback:
                ball = GameSprite('jungleball.png',400,200,10,50,50)
            if current_bg == background67:
                ball = GameSprite('ball67.png',400,200,10,50,50)
            if current_bg == scaryback:
                ball = GameSprite('scaryball.png',400,200,10,50,50)
        if ball.rect.x > 550:
            count1 +=1
            if current_bg == futureback:
                ball = GameSprite('ball.png',400,200,10,50,50)
            if current_bg == jungleback:
                ball = GameSprite('jungleball.png',400,200,10,50,50)
            if current_bg == background67:
                ball = GameSprite('ball67.png',400,200,10,50,50)
            if current_bg == scaryback:
                ball = GameSprite('scaryball.png',400,200,10,50,50)
        if count1 >=10:
            win1 = font1.render('Игрок 1 ПОБЕДИЛ!!!', True, (0,255,0))
            window.blit(win1, (100,150))
            speed_w = 0
            speed_h = 0
        if count2 >=10:
            win2 = font1.render('Игрок 2 ПОБЕДИЛ!!!', True, (0,255,0))
            window.blit(win2, (100,150))
            speed_w = 0
            speed_h = 0
    
        
    for e in event.get():
        if e.type == QUIT:
            game = False 
        elif e.type == KEYDOWN:
            if e.key== K_SPACE:
                paused = not paused
    clock.tick(FPS)
    display.update()