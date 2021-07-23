import pygame
import sys
import random
from pygame.locals import *


def pipe_animation():
	global game_over
	for pipe in PIPES:
		if pipe.top < 0:
			flipped_pipe = pygame.transform.flip(pipe_image, False, True)
			screen.blit(flipped_pipe, pipe)
		else:
			screen.blit(pipe_image, pipe)

		pipe.centerx -= 3

		if pipe.right < 0:
			PIPES.remove(pipe)


		if bird_rect.colliderect(pipe):
			game_over = True

def draw_floor():
	screen.blit(floor_image, (floor_x, 505))
	screen.blit(floor_image, (floor_x+448, 505))	

def create_pipes():
	pipe_y = random.choice(pipe_height)
	top_pipe = pipe_image.get_rect(midbottom=(467, pipe_y-200))
	bottom_pipe = pipe_image.get_rect(midtop=(467, pipe_y))
	return top_pipe, bottom_pipe

def draw_score(game_state):
	if game_state == "game_on":
			score_text = score_font.render(str(score), True, (255,255,255))
			score_rect = score_text.get_rect(center=(WIDTH//2, 66))
			screen.blit(score_text, score_rect)
	elif game_state == "game_over":
			score_text = score_font.render(f"Score: {score}", True, (255,255,255))
			score_rect = score_text.get_rect(center=(WIDTH//2, 66))
			screen.blit(score_text, score_rect)

			high_score_text = score_font.render(f"High Score: {high_score}", True, (255,255,255))
			high_score_rect = high_score_text.get_rect(center=(WIDTH//2, 440))
			screen.blit(high_score_text, high_score_rect)

def score_update():
	global score, is_score_time, high_score
	if PIPES:
		for pipe in PIPES:
			if 65 < pipe.centerx < 69 and is_score_time:
				score += 1
				is_score_time = False

			if pipe.left <= 0:
				is_score_time = True

	if score > high_score:
		high_score = score

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 288, 610
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
background_image = pygame.image.load("D:\\Codes\\Python\\PROJECTS\\TSSPython_20B030018\Week 3\\flappy_assets\\background.png").convert()
floor_image = pygame.image.load("D:\\Codes\\Python\\PROJECTS\\TSSPython_20B030018\Week 3\\flappy_assets\\floor.png").convert()
floor_x = 0
bird_image = pygame.image.load("D:\\Codes\\Python\\PROJECTS\\TSSPython_20B030018\Week 3\\flappy_assets\\bluebird.png").convert_alpha()

BIRD_FLAP = pygame.USEREVENT
pygame.time.set_timer(BIRD_FLAP, 100)

score = 0
high_score = 0
is_score_time = True
score_font = pygame.font.Font('D:\\Codes\\Python\\PROJECTS\\TSSPython_20B030018\Week 3\\flappy_assets\\04B_19.ttf', 27)

bird_rect = bird_image.get_rect(center=(67, 622//2))

bird_movement = 0
gravity = 0.098

pipe_image = pygame.image.load("D:\\Codes\\Python\\PROJECTS\\TSSPython_20B030018\Week 3\\flappy_assets\\pipe.png").convert_alpha()
pipe_height = [210, 280, 350, 400, 490]

PIPES = []
CREATE_PIPES = pygame.USEREVENT+1
pygame.time.set_timer(CREATE_PIPES, 1000)

game_over = False
game_over_image = pygame.image.load("D:\\Codes\\Python\\PROJECTS\\TSSPython_20B030018\Week 3\\flappy_assets\\message.png").convert_alpha()
game_over_rect = game_over_image.get_rect(center=(WIDTH//2,(HEIGHT//2)-40))

while True:
	clock.tick(120)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type == KEYDOWN:
			if event.key == K_SPACE and not game_over:
				bird_movement = 0
				bird_movement = -3

			if event.key == K_SPACE and game_over:
				game_over = False
				PIPES = []
				bird_movement = 0
				bird_rect = bird_image.get_rect(center=(67, 622//2))
				is_score_time = True
				score = 0

		if event.type == BIRD_FLAP:
			bird_rect = bird_image.get_rect(center=bird_rect.center)

		if event.type == CREATE_PIPES:
			PIPES.extend(create_pipes())

	screen.blit(background_image, (0,0))
	if not game_over:

		bird_movement += gravity

		bird_rect.centery += bird_movement

		rotated_bird = pygame.transform.rotozoom(bird_image, bird_movement * -6, 1)


		if bird_rect.top <= 5:
			game_over = True

		if bird_rect.bottom >=505:
			game_over =True

		
		screen.blit(rotated_bird, bird_rect)
		pipe_animation()
		score_update()
		draw_score("game_on")

	elif game_over:
		screen.blit(game_over_image, game_over_rect)
		draw_score("game_over")

	floor_x -= 1

	if floor_x < -50:
		floor_x = 0

	draw_floor()
	pygame.display.update()