import pygame
import sys
import random
import pygame.freetype

pygame.init()

screen = pygame.display.set_mode((1000, 600))
title = (pygame.display.set_caption("The Snow Runner"))
icon = pygame.image.load("D:\SantaClaus/Idle (3).png")
pygame.display.set_icon(icon)
rand = random.randint(0, 3)
c=0
finalMessageGood = ["Молодец!", "Ты крут", "Ты набрал так много очков, я твой фанат!", "Офигеть, ты так круто играешь!"]
finalMessageBad = ["В следущий раз наберешь больше очков!", "Не растраивайся, играть в эту игру ты только учишься!", "Ты мог и лучше!", "Ты набрал мало очков, попробуй сыграть еще раз!"]
finalMessageGreat = ["Как ты набрал более 5000 очков?", "Ты великолепный!", "Я даю тебе звание PRO", "Ты очень молодец!"]
run = True
font = pygame.freetype.Font(None, 36)
clock = pygame.time.Clock()
ov = [176, 0, 0]
s_x = 0
y = 500
width = 100
ps = 0
height = 100
speed = 7
isJump = False
jumpCount = 12
left = False
right = False
up = False
animationCount = 0
lastMoveRight = False
lastMoveLeft = False
jumpAnimCount = 0
jumpLeftF = False
jumpRightF = False
bg = pygame.image.load("images/bg.png").convert_alpha()
bg_x = 0

goRight = [pygame.image.load("images/SantaClaus/Run (1) 1.png").convert_alpha(),
           pygame.image.load("images/SantaClaus/Run (2) 1.png").convert_alpha(),
           pygame.image.load("images/SantaClaus/Run (3) 1.png").convert_alpha(),
           pygame.image.load("images/SantaClaus/Run (4) 1.png").convert_alpha(),
           pygame.image.load("images/SantaClaus/Run (5) 1.png").convert_alpha(),
           pygame.image.load("images/SantaClaus/Run (6) 1.png").convert_alpha(),
           pygame.image.load("images/SantaClaus/Run (7) 1.png").convert_alpha(),
           pygame.image.load("images/SantaClaus/Run (8) 1.png").convert_alpha(),
           pygame.image.load("images/SantaClaus/Run (9) 1.png").convert_alpha(),
           pygame.image.load("images/SantaClaus/Run (10) 1.png").convert_alpha(),
           pygame.image.load("images/SantaClaus/Run (11) 1.png").convert_alpha()]

goLeft = [pygame.image.load("images/SantaClaus/RunLeft (1) 1.png").convert_alpha(),
          pygame.image.load("images/SantaClaus/RunLeft (2) 1.png").convert_alpha(),
          pygame.image.load("images/SantaClaus/RunLeft (3) 1.png").convert_alpha(),
          pygame.image.load("images/SantaClaus/RunLeft (4) 1.png").convert_alpha(),
          pygame.image.load("images/SantaClaus/RunLeft (5) 1.png").convert_alpha(),
          pygame.image.load("images/SantaClaus/RunLeft (6) 1.png").convert_alpha(),
          pygame.image.load("images/SantaClaus/RunLeft (7) 1.png").convert_alpha(),
          pygame.image.load("images/SantaClaus/RunLeft (8) 1.png").convert_alpha(),
          pygame.image.load("images/SantaClaus/RunLeft (9) 1.png").convert_alpha(),
          pygame.image.load("images/SantaClaus/RunLeft (10) 1.png").convert_alpha(),
          pygame.image.load("images/SantaClaus/RunLeft (11) 1.png").convert_alpha()]

jumpRight = [pygame.image.load("images/SantaClaus/Jump (1) 1.png").convert_alpha(),
             pygame.image.load("images/SantaClaus/Jump (2) 1.png").convert_alpha(),
             pygame.image.load("images/SantaClaus/Jump (3) 1.png").convert_alpha(),
             pygame.image.load("images/SantaClaus/Jump (4) 1.png").convert_alpha(),
             pygame.image.load("images/SantaClaus/Jump (5) 1.png").convert_alpha(),
             pygame.image.load("images/SantaClaus/Jump (6) 1.png").convert_alpha(),
             pygame.image.load("images/SantaClaus/Jump (7) 1.png").convert_alpha(),
             pygame.image.load("images/SantaClaus/Jump (8) 1.png").convert_alpha(),
             pygame.image.load("images/SantaClaus/Jump (9) 1.png").convert_alpha(),
             pygame.image.load("images/SantaClaus/Jump (10) 1.png").convert_alpha(),
             pygame.image.load("images/SantaClaus/Jump (11) 1.png").convert_alpha(),
             pygame.image.load("images/SantaClaus/Jump (12) 1.png").convert_alpha(),
             pygame.image.load("images/SantaClaus/Jump (13) 1.png").convert_alpha(),
             pygame.image.load("images/SantaClaus/Jump (14) 1.png").convert_alpha(),
             pygame.image.load("images/SantaClaus/Jump (15) 1.png").convert_alpha(),
             pygame.image.load("images/SantaClaus/Jump (16) 1.png").convert_alpha()]

jumpLeft = [pygame.image.load("images/SantaClaus/JumpLeft (1) 1.png").convert_alpha(),
            pygame.image.load("images/SantaClaus/JumpLeft  (2) 1.png").convert_alpha(),
            pygame.image.load("images/SantaClaus/JumpLeft  (3) 1.png").convert_alpha(),
            pygame.image.load("images/SantaClaus/JumpLeft  (4) 1.png").convert_alpha(),
            pygame.image.load("images/SantaClaus/JumpLeft  (5) 1.png").convert_alpha(),
            pygame.image.load("images/SantaClaus/JumpLeft  (6) 1.png").convert_alpha(),
            pygame.image.load("images/SantaClaus/JumpLeft  (7) 1.png").convert_alpha(),
            pygame.image.load("images/SantaClaus/JumpLeft  (8) 1.png").convert_alpha(),
            pygame.image.load("images/SantaClaus/JumpLeft  (9) 1.png").convert_alpha(),
            pygame.image.load("images/SantaClaus/JumpLeft  (10) 1.png").convert_alpha(),
            pygame.image.load("images/SantaClaus/JumpLeft  (11) 1.png").convert_alpha(),
            pygame.image.load("images/SantaClaus/JumpLeft  (12) 1.png").convert_alpha(),
            pygame.image.load("images/SantaClaus/JumpLeft  (13) 1.png").convert_alpha(),
            pygame.image.load("images/SantaClaus/JumpLeft  (14) 1.png").convert_alpha(),
            pygame.image.load("images/SantaClaus/JumpLeft  (15) 1.png").convert_alpha(),
            pygame.image.load("images/SantaClaus/JumpLeft  (16) 1.png").convert_alpha()]

idle = [pygame.image.load("images/SantaClaus/Idle (1) 1.png").convert_alpha()]
idleLeft = [pygame.image.load("images/SantaClaus/IdleLeft  (1).png").convert_alpha()]

SnowManWalk = [pygame.image.load("images/SnowMan/Walk/walk1 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk2 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk3 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk4 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk5 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk6 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk7 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk8 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk9 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk1 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk2 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk3 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk4 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk5 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk6 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk7 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk8 1.png").convert_alpha(),
               pygame.image.load("images/SnowMan/Walk/walk9 1.png").convert_alpha()]

SnowManWalkLeft = [pygame.image.load("images/SnowMan/Walk/walk1Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk2Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk3Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk4Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk5Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk6Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk7Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk8Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk9Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk1Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk2Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk3Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk4Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk5Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk6Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk7Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk8Left 1 (1).png"),
                   pygame.image.load("images/SnowMan/Walk/walk9Left 1 (1).png")]
vil_x = 1020
vil_y = 430
vil_speed = 5
vilAnimCount = 0
vilArr = []
vilRectX = 1020
vil_timer = pygame.USEREVENT + 1
pygame.time.set_timer(vil_timer, 2000)

snow = pygame.image.load("images/snow.png").convert_alpha()
snow_x = 0
snow_y = 500

village = pygame.image.load("images/village.png").convert_alpha()
village_x = 0
village_y = 40
numbers = 0
slow = 0
count = 0
counter_hearts = 0
gameOver = pygame.image.load("images/GameOver.png").convert_alpha()
heart = pygame.image.load("images/heart.png").convert_alpha()
run2 = True

def AllDraw():
    global run
    global bg_x
    global counter_hearts
    global animationCount
    global c
    global snow_x
    global village_x
    global vil_x
    global vilAnimCount
    global vilRectX
    global jumpAnimCount
    global s_x
    global y
    global village_y
    global finalCaption
    global run2
    global count
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1000, 0))

    screen.blit(village, (village_x, village_y))
    screen.blit(village, (village_x + 1000, village_y))

    screen.blit(snow, (snow_x - 1000, snow_y))
    screen.blit(snow, (snow_x, snow_y))
    screen.blit(snow, (snow_x+1000, snow_y))

    santa_rect = goLeft[0].get_rect(topleft=(s_x, y))
    if run2:
        count += 1

    if run2:
        if animationCount >= 30:
            animationCount = 0

        if jumpAnimCount >= 30:
            jumpAnimCount = 0

        if left:
            screen.blit(goLeft[animationCount // 3], (s_x, y))
            animationCount += 1
            bg_x += 0.5
            snow_x += 2
            village_x += 1

        elif right:
            screen.blit(goRight[animationCount // 3], (s_x, y))
            animationCount += 1
            bg_x -= 0.5
            snow_x -= 2
            village_x -= 1
            if bg_x == -1000:
                bg_x = 0
            if snow_x == -1000:
               snow_x = 0
            if village_x == -1000:
                village_x = 0

        elif jumpLeftF:
            screen.blit(jumpLeft[jumpAnimCount // 3], (s_x, y))
            jumpAnimCount += 1

        elif jumpRightF:
            screen.blit(jumpRight[jumpAnimCount // 3], (s_x, y))
            jumpAnimCount += 1

        else:
            if lastMoveLeft == True and lastMoveRight == False:
                screen.blit(idleLeft[animationCount // 2], (s_x, y))
                animationCount += 1
            else:
                screen.blit(idle[animationCount // 2], (s_x, y))
                animationCount += 1

        if vilAnimCount >= 30:
            vilAnimCount = 0
        else:
            vilAnimCount += 1

        for i in vilArr:
            screen.blit(SnowManWalk[vilAnimCount//3], i)
            i.x -= vil_speed
            if santa_rect.colliderect(i):
                counter_hearts += 1

        if counter_hearts == 0:
            screen.blit(heart, (20, 30))
            screen.blit(heart, (70, 30))
            screen.blit(heart, (120, 30))
            font.render_to(screen, (780, 30), "Points: " + str(count), (255, 255, 255))
        elif counter_hearts > 0 and counter_hearts <= 41:
            screen.blit(heart, (20, 30))
            screen.blit(heart, (70, 30))
            font.render_to(screen, (780, 30), "Points: " + str(count), (255, 255, 255))
        elif counter_hearts > 0 and  counter_hearts > 41 and counter_hearts <= 82:
            screen.blit(heart, (20, 30))
            c += 1
            font.render_to(screen, (780, 30), "Points: " + str(count), (255, 255, 255))
        else:
            if c == 1:
                run2 = False
                screen.fill(ov)
                font.render_to(screen, (405, 20), "Points: " + str(count), (255, 255, 255))
                screen.blit(gameOver, (330, 100))
                if (count >= 2000) and count < 5000:
                    print(finalMessageGood[rand])
                elif count < 2000:
                    print(finalMessageBad[rand])
                elif count > 5000:
                    print(finalMessageGreat[rand])
            if keys[pygame.K_1]:
                c = 0


        pygame.display.update()

while run:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        if event.type == vil_timer:
            vilArr.append(SnowManWalk[0].get_rect(topleft=(1020, 430)))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and s_x > snow_x:
        if s_x > 0:
            s_x -= speed
            left = True
            right = False
            lastMoveLeft = True
            lastMoveRight = False
        else:
            left = True
            right = False
            lastMoveLeft = True
            lastMoveRight = False

    elif keys[pygame.K_RIGHT]:
        if s_x < 700:
            s_x += speed
            left = False
            right = True
            lastMoveLeft = False
            lastMoveRight = True
        else:
            left = False
            right = True
            lastMoveLeft = False
            lastMoveRight = True

    else:
        left = False
        right = False
        animationCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            if lastMoveLeft == True:
                jumpLeftF = True
                jumpRightF = False
            elif lastMoveRight == True:
                jumpRightF = True
                jumpLeftF = False
    else:
        if jumpCount >= -12:
            if jumpCount < 0:
                y += (jumpCount ** 2) // 2
            else:
                y -= (jumpCount ** 2) // 2
            jumpCount -= 1
        else:
            isJump = False
            jumpLeftF = False
            jumpRightF = False
            jumpCount = 12
    AllDraw()
