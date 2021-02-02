import pygame as pg
import sys
from pygame import mixer
pg.init()
pg.display.set_caption('Дровосек')
pg.mixer.music.load('Scott Lloyd Shelly — Terraria OST.mp3')
pg.mixer.music.play()
pg.mixer.music.set_volume(0.05)
f = open('teext.txt', 'r+')
a = f.readlines()[-1].split()
W = 1380
H = 750
sc = pg.display.set_mode((W, H))
sc.fill((100, 150, 200))
dog_surf = pg.image.load('48350adcdc6aa00fc401ce224ebc7e41.jpg')
wood = pg.image.load("8275b67b3544d58.png")
left = pg.image.load("c1b6a740d224c42.png")
right = pg.image.load("122.png")
money = pg.image.load("90bdec8f41569bc.png")
x = 150
player = left
coins = float(a[0])
bank = int(a[1])
maxi = int(a[2])
cps = float(a[3])
maxi1 = int(a[4])
vvv = int(a[5])
bbb = int(a[6])
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            f.seek(0)
            f.truncate()
            f.write(str(f'{coins} {bank} {maxi} {cps} {maxi1} {vvv} {bbb}'))
            sys.exit()
        keys = pg.key.get_pressed()
        pressed = pg.mouse.get_pressed()
        if i.type == pg.MOUSEBUTTONDOWN:
            coins += bank
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_p:
                if i.key == pg.K_p:
                    mixer.music.pause()
            if i.key == pg.K_b and coins >= 2500 and maxi == 0:
                bank = 1
                coins -= 2500
                maxi += 1
                bbb = 25000
            if i.key == pg.K_b and coins >= 25000 and maxi == 1:
                bank = 6
                coins -= 25000
                maxi += 1
                bbb = 100000
            if i.key == pg.K_b and coins >= 100000 and maxi == 2:
                bank = 20
                coins -= 100000
                maxi += 1
                bbb = 250000
            if i.key == pg.K_b and coins >= 250000 and maxi == 3:
                bank += 45
                coins -= 250000
                maxi += 1
                bbb = 25000000
            if i.key == pg.K_b and coins >= 25000000 and maxi == 4:
                bank += 500
                coins -= 25000000
                maxi += 1
                bbb = 25000000000000
            if i.key == pg.K_b and coins >= 25000000000000 and maxi == 5:
                bank = 99999999999999
                coins -= 25000000000000
                maxi += 1
                bbb = 'max'
            if i.key == pg.K_v and coins >= 100 and maxi1 == 0:
                maxi1 += 1
                cps = 0.4
                coins -= 100
                vvv = 2000
            if i.key == pg.K_v and coins >= 2000 and maxi1 == 1:
                maxi1 += 1
                cps += 2.5
                coins -= 2000
                vvv = 15000
            if i.key == pg.K_v and coins >= 15000 and maxi1 == 2:
                maxi1 += 1
                cps += 8.7
                coins -= 15000
                vvv = 55000
            if i.key == pg.K_v and coins >= 55000 and maxi1 == 3:
                cps += 20.4
                coins -= 55000
                maxi1 += 1
                vvv = 100000
            if i.key == pg.K_v and coins >= 100000 and maxi1 == 4:
                cps += 99.9
                coins -= 100000
                maxi1 += 1.0
                vvv = 1000000
            if i.key == pg.K_v and coins >= 1000000 and maxi1 == 4:
                cps += 999.9
                coins -= 1000000
                maxi1 += 1
                vvv = 'Max'
    if keys[pg.K_a]:
        if x >= 25:
            x -= 10
            x -= 15
        player = left
    elif keys[pg.K_d]:
        if x <= 1355:
            x += 10
            x += 15
        player = right
    coins = coins + cps
    font = pg.font.Font(None, 60)
    text = font.render(str(int(coins)), True, (255, 255, 255))
    place = text.get_rect(center=(250, 650))
    font1 = pg.font.Font(None, 50)
    text1 = font1.render(f" 'v' - для повышения click: {vvv}        текущее - {str(int(cps * 10))}", True, (255, 255, 255))
    place1 = text1.get_rect(center=(900, 670))
    font2 = pg.font.Font(None, 50)
    text2 = font2.render(f" 'b' - для повышения cps: {bbb}        текущее - {int(bank)}", True, (255, 255, 255))
    place2 = text2.get_rect(center=(900, 640))
    font3 = pg.font.Font(None, 50)
    text3 = font3.render(f"P выкл", True, (255, 255, 255))
    place3 = text3.get_rect(center=(900, 610))
    money_scale = pg.transform.scale(money, (money.get_width() // 10, money.get_height() // 10))
    money_rect = money_scale.get_rect(center=(80, 650))
    scale = pg.transform.scale(dog_surf, (dog_surf.get_width() * 5 // 2, dog_surf.get_height() * 3 // 2))
    scale_rect = scale.get_rect(center=(200, 150))
    wood_scale = pg.transform.scale(wood, (wood.get_width() // 2, wood.get_height() // 2))
    player_scale = pg.transform.scale(player, (player.get_width() // 6, player.get_height() // 6))
    player_rect = player_scale.get_rect(center=(x, 481))
    wood_rect = wood_scale.get_rect(center=(900, 305))
    sc.blit(scale, scale_rect)
    sc.blit(wood_scale, wood_rect)
    sc.blit(player_scale, player_rect)
    sc.blit(text, place)
    sc.blit(money_scale, money_rect)
    sc.blit(text1, place1)
    sc.blit(text2, place2)
    sc.blit(text3, place3)
    pg.display.update()
    pg.time.delay(100)