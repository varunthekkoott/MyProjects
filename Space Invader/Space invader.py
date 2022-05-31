import pygame
import random
import math
import Simple


def show_score(x, y):
    the_score = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(the_score, (x, y))


def player(x, y):
    screen.blit(player1, (x, y))


def enemy(x, y, i):
    screen.blit(enemy1[i], (x, y))


def fire_bullet(x, y, thebullet):
    global bullet_state
    bullet_state = "fire"
    screen.blit(thebullet, (x+16, y+20))


def iscollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx-bulletx,2)) + (math.pow(enemyy-bullety, 2)))
    if distance < 27:
        return True
    else:
        return False


def game_over():
    the_over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(the_over_text, (200, 250))


print("How to play:\nPress the right or left arrow buttons to move your spaceship around.\nPress the down arrow or the spacebar to launch a bullet\nYou can only launch another bullet after the first bullet has hit the enemy or gone out of the screen\nIf an enemy(UFO) comes too down the game will get over")
while True:
    difficulty = input("\nWhat difficulty do you want (number) : ")
    check = Simple.checktype(difficulty, int)
    if check:
        break
    else:
        pass

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('Capture.PNG')
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)

player1 = pygame.image.load("Capture.PNG")
player1 = pygame.transform.scale(player1, (64, 64))
playerX = 370
playerY = 480
playerX_change = 0

enemy1 = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = int(difficulty)

for i in range(num_of_enemy):
    enemy555 = pygame.image.load("Capture1.PNG")
    enemy1.append(pygame.transform.scale(enemy555, (64, 64)))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(30)

bullet1 = pygame.image.load("Capture2.PNG")
bullet1 = pygame.transform.scale(bullet1, (16, 20))
bulletX = 0
bulletY = 440
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 70)
textX = 10
textY = 10

running = True
while running:

    screen.fill((0, 0, 0))
    background1 = pygame.image.load("Capture3.PNG")
    background1 = pygame.transform.scale(background1, (800, 600))
    screen.blit(background1, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE or event.key == pygame.K_DOWN:
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX+10, bulletY+10, bullet1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX < 0:
        playerX = 0
    if playerX > 736:
        playerX = 736

    for i in range(num_of_enemy):
        if enemyY[i] > 420:
            for j in range(num_of_enemy):
                enemyY[j] = 2000
            game_over()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] < 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        if enemyX[i] > 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY, bullet1)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
