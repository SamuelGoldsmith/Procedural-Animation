import pygame
from Bone import Bone
from sys import exit
pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()

surface1 = pygame.Surface((1800,900))
surface1.fill('green')

mybone = Bone(52/2, (100,100))
children_size = [58, 40, 60, 68, 71, 65, 50, 28, 15, 11, 9, 7, 7]
body = [mybone]
current = mybone
for rad in children_size:
    current = current.add_child(rad/2)
    body.append(current)
# mybone.add_child(30).add_child(35).add_child(28).add_child(20).add_child(20)
print(mybone.center)
print(mybone.get_sides())
# morty = pygame.image.load('./morty.jpg')
speed_scale = 3
run = True
while(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if speed_scale > 1:
        speed_scale -= keys[pygame.K_q]/5
    speed_scale += keys[pygame.K_e]/5


    screen.blit(surface1,(0,0))

    if keys[pygame.K_d] == 1: mybone.rotate("right")
    if keys[pygame.K_a] == 1: mybone.rotate("left")
    if keys[pygame.K_w] == 1: mybone.move(speed_scale)
    mybone.draw_circle(screen, True)
    pygame.display.update()
    clock.tick(60)