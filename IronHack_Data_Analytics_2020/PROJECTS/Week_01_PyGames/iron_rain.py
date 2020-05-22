import pygame
import random
import math
from pygame import mixer



pygame.init()

#Creating a PyGame window
ascreen = pygame.display.set_mode((800, 600))

running = True

# Game window Title change
pygame.display.set_caption("IRON RAIN")

# Game window Icon change
# Load icon file
icon = pygame.image.load("logo_iron_sm.png")
# Set file as window icon
pygame.display.set_icon(icon)

#Load Rain
iron_img = pygame.image.load("ironhacker.png")
# Set image Position
iron_x = 365
iron_y = 500

#iron movement
iron_x_change = 0


#Multiple jobs
job_img = []
job_x = []
job_y = []
job_x_change = []
job_y_change = []
num_of_jobs = 4

for x in range(num_of_jobs):
    job_img.append(pygame.image.load("job_offer_1.png"))
    job_x.append(random.randint(65, 735))
    job_y.append(random.randint(0, 50))
    job_x_change.append(1)
    job_y_change.append(2)

def iron(x, y):
    ascreen.blit(iron_img, (x, y))

def job(x, y, i):
    ascreen.blit(job_img[i], (x, y))

def isCollision(job_x, job_y, iron_x, iron_y):
    #This is the formula of Distance between to points
    distance = math.sqrt(math.pow(job_x - iron_x, 2) + math.pow(job_y - iron_y, 2))
    if distance < 40:
        return True
    else:
        return False


player_score = 0
font = pygame.font.Font("freesansbold.ttf", 24)
text_x = 10
text_y = 10

start_time = pygame.time.get_ticks()
stop_time = 40 * 1000

def show_score(x, y):
    score = font.render(f"Score: {player_score}", True, (255, 255, 255))
    ascreen.blit(score, (x, y))


# Game Over Text
over_font = pygame.font.Font("freesansbold.ttf", 64)

def time_over():
    for k in range(num_of_jobs):
        job_y[k] = 2000
    over_text = over_font.render(f"GAME OVER", True, (255, 0, 0))
    ascreen.blit(over_text, (200, 250))



# Game Loop
while running:
#Changing screen background color
    background_image = pygame.image.load("fundo.png")
    ascreen.blit(background_image, (0, 0))
    # ascreen.fill((55, 55, 55))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                iron_x_change = -1
            elif event.key == pygame.K_RIGHT:
                iron_x_change = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                iron_x_change = 0

    current_time = pygame.time.get_ticks()
    if (current_time - start_time) >= stop_time:
        time_over()

    iron_x += iron_x_change
# Setting boundaries
    if iron_x <= 0:
        iron_x = 0
    elif iron_x >= 735:
        iron_x = 735

# Setting boundaries of the rain
# Rain movement
    for i in range(num_of_jobs):

        job_y[i] += job_y_change[i]
        if job_y[i] >= 500:
            #num_of_aliens += 1
            job_x[i] = random.randint(65, 735)
            job_y[i] = random.randint(0, 50)
            job(job_x[i], job_y[i], i)
        elif job_y[i] >= 550:
            job_y[i] = 2000

         #Collision Algor - When there is a collision the laser position resets
         #Formula of Distance between two points
        collision = isCollision(job_x[i], job_y[i], iron_x, iron_y)
        if collision:
            job_y[i] = 0
            #num_of_aliens += 1
            player_score += 1
            job_x[i] = random.randint(65, 735)
            job_y[i] = random.randint(0, 50)
        job(job_x[i], job_y[i], i)

    iron(iron_x, iron_y)
    show_score(text_x, text_y)
    pygame.display.update()
pygame.quit()
