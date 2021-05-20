import pygame
import random
import math

#initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load(r'E:\WORK\python\games\space invader\background.png')

#title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(r'E:\WORK\python\games\space invader\rocket.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load(r'E:\WORK\python\games\space invader\space-invaders.png')
playerX = 400
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x,y))

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):


    enemyImg.append(pygame.image.load(r'E:\WORK\python\games\space invader\alien.png'))
    enemyX.append(random.randint(0,734))
    enemyY.append(random.randint(50,200))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))


#bullet
bulletImg = pygame.image.load(r'E:\WORK\python\games\space invader\bullet.png')
bulletX = 0
bulletY = 420
bulletX_change = 0
bulletY_change = 0.75
bullet_state = "ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16, y+10))

#collision
def isCollision(enemyX,enemyY, bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY- bulletY, 2)) )
    if distance <27:
        return True
    else:
        return False

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 0

def show_score(x,y):
    score = font.render("Score : "+ str(score_value), True,(255,255,255))
    screen.blit(score, (x,y))


over_font = pygame.font.Font('freesansbold.ttf',32)
def game_over_text():
    over_text = over_font.render("Game Over", True, (0,0,0))
    screen.blit(over_text, (300,200))

#game loop
running = True
while running:
    #screen color (RGB)
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #if any key is pressed check if its left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    #boundary check
    playerX += playerX_change
    if playerX <=0:
        playerX =0
    elif playerX >=736:
        playerX = 736
    #enemy movement
    for i in range(num_of_enemies):

        #game over
        if enemyY[i] > 420:
            for j in range(num_of_enemies):
                enemyY[j] = 2000

            game_over_text()
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i] =0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >=736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

    #collision
        collision = isCollision(enemyX[i],enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 10
            enemyX[i] = random.randint(0,734)
            enemyY[i] = random.randint(50,200)
        enemy(enemyX[i],enemyY[i], i)



    #Bullet Movement
    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    



    player(playerX, playerY)
    show_score(textX, textY)
    
    pygame.display.update()