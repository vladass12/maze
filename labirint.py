# Разработай свою игру в этом файле!
from pygame import *

window = display.set_mode((700,500))
display.set_caption('GAME')
background = transform.scale(image.load('1614854855_173-p-foni-mainkraft-dlya-shapki-yutuba-235.jpg'), (700, 500))
run = True
win_image = transform.scale(image.load(
'1679527321_uhd-name-p-strashnie-volosi-vkontakte-26.jpg'), (700, 500))
lose_image = transform.scale(image.load('1664481451_new_preview_1oPkLt.jpg'), (700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self, image1, player_x, player_y,size_x, size_y): 
          super().__init__()
          self.image = transform.scale(image.load(image1), (size_x, size_y))
          self.rect = self.image.get_rect()
          self.rect.x = player_x
          self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, image1, player_x, player_y,size_x, size_y, x_speed, y_speed):
        super().__init__(image1, player_x, player_y,size_x, size_y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        if player.rect.x <= 620 and player.x_speed > 0 or player.rect.x >= 0 and player.x_speed < 0:
            self.rect.x += self.x_speed
        if player.rect.y <= 450 and player.y_speed > 0 or player.rect.y >= 0 and player.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, walls, False)
        if self.x_speed > 0:
            for p in platforms_touched:
               self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def fire(self):
        bullet = Bullet('Без названия (1).png', self.rect.right, self.rect.centery, 15, 20,18)
        bullet.add(bullet)
class Bullet(GameSprite):
    def __init__(self, image1, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(image1, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 700:
            self.kill()

class Enemy(GameSprite):
    def __init__(self, image1,player_x, player_y, size_x, size_y, player_speed):
        super().__init__(image1, player_x,player_y, size_x, size_y)
        self.speed = player_speed
        self.direction = 'left'
    def update(self):
        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= 620:
            self.direction = 'left'
        if self.direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

player = Player('23735086-dces7k7r-v4.jpg', 5, 420, 80, 80, 0, 0)     
w1 = GameSprite('wall.png', 700 / 2 - 700 / 3, 250, 300, 50)
w2 = GameSprite('wall.png', 370, 100, 80, 400)
final = GameSprite('1684530984_mykaleidoscope-ru-p-tort-salli-feis-instagram-77.jpg', 615, 400, 80, 80)
finish = False
monster = Enemy('1680375582_kartinki-pibig-info-p-kartinka-prikol-bespilotniki-arti-70.jpg', 615, 300, 80, 80, 5)
while run:
    walls = sprite.Group()
    bullets = sprite.Group()
    monsters = sprite.Group()
    monsters.add(monster)
    walls.add(w1)
    walls.add(w2)

    time.delay(50)
    
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                player.y_speed = -5
            elif e.key == K_s:
                player.y_speed = 5
            elif e.key == K_a:
                player.x_speed = -5
            elif e.key == K_d:
                player.x_speed = 5
            elif e.key == K_SPACE:
                player.fire()
        elif e.type == KEYUP:
            if e.key == K_w:
                player.y_speed = 0
            elif e.key == K_s:
                player.y_speed = 0
            elif e.key == K_a:
                player.x_speed = 0
            elif e.key == K_d:
                player.x_speed = 0
    if finish != True:
        window.blit(background,(0,0))
        walls.draw(window)
        bullets.draw(window)
        monsters.update()
        monsters.draw(window)
        w2.reset()
        player.reset()
        player.update()
        bullets.update()
        final.reset()
        sprite.groupcollide(monsters, bullets, True, True)
        sprite.groupcollide(bullets, walls, True, False)
        if sprite.collide_rect(player, final):
            window.blit(win_image, (0, 0))
            finish = True
        if sprite.collide_rect(player, monster):
            window.blit(lose_image, (0, 0))
            finish = True
    display.update()
    
