import pygame, sys, random 

pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()
game_font = pygame.font.SysFont(None,40)


gravity = 0.25
bird_movement = 0
game_active = True
score = 0
floor_x_pos = 0

#Load the necessary images

bg_surface = pygame.image.load('flappy_assets/background.png')
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('flappy_assets/floor.png')
floor_surface = pygame.transform.scale2x(floor_surface)

bird_surface = pygame.transform.scale2x(pygame.image.load('flappy_assets/bluebird.png'))
bird_rect = bird_surface.get_rect(center = (100,512))

pipe_surface = pygame.image.load('flappy_assets/pipe.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)

game_over_surface = pygame.transform.scale2x(pygame.image.load('flappy_assets/message.png'))
game_over_rect = game_over_surface.get_rect(center = (288,512))


pipe_list = [i for i in range(10000)]

# We have created this custom event which will be automatically trigerred according to the time set
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [400,600,800]





def create_pipe(pipe_list):
	pipes = []
	pipe_rect_list = []
	for i in range(len(pipe_list)):
    		pipes = pipes  + [pygame.image.load('pipe.png')]
    		pipe_rect_list  = pipe_rect_list + [pipes[i].get_rect(topleft = [576 + (10*i), 800])]
	return pipes, pipe_rect_list


def move_pipes(pipe_rect_list):
	for i in range(len(pipe_rect_list)):
    		pipe_rect_list[i].left += 5
	return pipe_rect_list


def draw_pipes(pipes, pipe_rect_list):
    	for i in range(len(pipe_rect_list)):
    			screen.blit(pipes[i], pipe_rect_list[i])



def draw_floor():
	"""Draw the floor surfaces on the screen. Hint: Use 2 floor surfaces to ensure proper motion of the floor"""







def check_collision(pipes):
	"""
	check whether the bird might have collided with any of the pipes you can use
	colliderect(). Or the bird might have hit the floor or crossed the top.
	"""









def score_display(game_state):
	"""
	display the score on the screen. Note depending on what the game state is 
	score will have to be displayed at different places.
	"""







def check_for_events():
	"""
	Will contain main for loop listening for events. It should have code to respond to 
	quitting, pressing the spacebar(if game is active it causes the jump, use bird_movement attribute and if not
	it should turn the game active and start it). It should also listen for the SPAWNPIPE event 
	"""








def update_bird(pipe_list):
	"""
	Update the postion of the bird, update the bird_movement variable for gravity, 
	check for collisions with the pipes
	"""





def update_pipes(pipe_list, pipes, pipe_rect_list):
	move_pipes(pipe_rect_list)
	draw_pipes(pipes, pipe_rect_list)



def update_score():
	"""
	Update the score if the bird has passed through the opening
	"""





comp_list = create_pipe(pipe_list)

while True:
	check_for_events()
	screen.blit(bg_surface,(0,0))

	if game_active:
		update_bird(pipe_list)
		update_pipes(pipe_list, comp_list[0], comp_list[1])

		update_score()
		score_display('main_game')
		
	else:
		screen.blit(game_over_surface,game_over_rect)
		score_display('game_over')


	# Change the position of the floor and draw it. Make sure if it reaches the left end reset it
	


	pygame.display.flip()

	# set the speed of the game
	clock.tick(120)
