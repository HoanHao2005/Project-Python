import pygame
import random
pygame.init()
screen=pygame.display.set_mode((600,300))
pygame.display.set_caption('dinosaur')
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
volume = 0.5
background_x=0
background_y=0
dinosaur_x=0
dinosaur_y=230
tree_x=550
tree_y=230
ngoisao_x = 600
ngoisao_y = random.randint(50, 150)
ngoisao_velocity = 3
x_velocity=5
y_velocity=7
score=0
font=pygame.font.SysFont('san',20)
font1=pygame.font.SysFont('san',40)
current_time = 0
time_interval = 1000
background=pygame.image.load('background.jpg')
dinosaur=pygame.image.load('dinosaur.png')
tree=pygame.image.load('tree.png')
ngoisao = pygame.image.load('star.png')
sound1=pygame.mixer.Sound('jump.wav')
sound1.set_volume(0.5)
sound2=pygame.mixer.Sound('point.wav')
sound2.set_volume(0.1)
sound3=pygame.mixer.music.load('nhac.mp3')
pygame.mixer.music.play(-1)
clock=pygame.time.Clock()
jump=False
running=True
pausing=False
while running:
  pygame.mixer.music.set_volume(volume)
  current_time += clock.get_time()
  if current_time >= time_interval:
    current_time = 0
    x_velocity += 0.1
  clock.tick(60)
  screen.fill(WHITE)
  background1_rect=screen.blit(background,(background_x,background_y))
  background2_rect=screen.blit(background,(background_x+600,background_y))
  score_txt=font.render('score:'+str(score),True,BLUE)
  screen.blit(score_txt,(5,5))
  ngoisao_x -= ngoisao_velocity
  if background_x+600<=0:
    background_x=0
  tree_x-=x_velocity
  if tree_x<=-20:
    tree_x= 600
    score+=1
  if ngoisao_x <= -50:
        ngoisao_x = 600
        ngoisao_y = random.randint(50, 150)
        ngoisao_velocity = random.randint(2, 5)
  screen.blit(ngoisao, (ngoisao_x, ngoisao_y))
  if 230>=dinosaur_y>=80:
    if jump==True:
      dinosaur_y-=y_velocity
  else:
    jump=False
  if dinosaur_y<230:
    if jump==False:
       dinosaur_y+=y_velocity
  ngoisao_rect=screen.blit(ngoisao,(ngoisao_x,ngoisao_y))
  dinosaur_rect=screen.blit(dinosaur,(dinosaur_x,dinosaur_y))
  tree_rect=screen.blit(tree,(tree_x,tree_y))
  background_x-=x_velocity
  if dinosaur_rect.colliderect(tree_rect):
    pygame.mixer.Sound.play(sound2)
    pausing=True
    gameover_txt=font1.render('GAME OVER',True,RED)
    screen.blit(gameover_txt,(200,100))
    x_velocity=0
    y_velocity=0

  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      running=False
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_SPACE:
        if dinosaur_y==230:
          pygame.mixer.Sound.play(sound1)
          jump=True
        if pausing:
          background_x=0
          background_y=0
          dinosaur_x=0
          dinosaur_y=230
          tree_x=550
          tree_y=230
          x_velocity=5
          y_velocity=7
          score=0
          pausing=False



  pygame.display.flip()
pygame.quit()