import pygame, sys, random
def run(slider_variables, spin_box_variables):
	ball_speed, player_speed, ball_size, player_size, rebound_y, x_acceleration = slider_variables

	class Block(pygame.sprite.Sprite):
		def __init__(self,x_pos,y_pos, width, height):
			super().__init__()
			self.rect = pygame.Rect(x_pos,y_pos, width, height)

	class Player(Block):
		def __init__(self, x_pos, y_pos, width, height, speed):
			super().__init__(x_pos,y_pos, width, height)
			self.speed = speed
			self.movement = 0

		def screen_constrain(self):
			if self.rect.top <= 0:
				self.rect.top = 0
			if self.rect.bottom >= screen_height:
				self.rect.bottom = screen_height

		def update(self):
			self.rect.y += self.movement
			self.screen_constrain()
   
	class Ball(Block):
		def __init__(self, x_pos, y_pos, width, height, speed_x, speed_y):
			super().__init__(x_pos, y_pos, width, height)
			self.default_speed_x = speed_x
			self.default_speed_y = speed_y
			self.speed_x = speed_x * random.choice((-1,1))
			self.speed_y = speed_y * random.choice((-1,1))
			self.active = False
			self.score_time = 0
    
		def update(self, player1, player2):
			if self.active:
				self.rect.x += self.speed_x
				self.rect.y += self.speed_y
				self.collisions(player1, player2)
			else:
				self.restart_counter()
			
		def collisions(self, player1, player2):
			if self.rect.top <= 0 or self.rect.bottom >= screen_height:
				pygame.mixer.Sound.play(plob_sound)
				self.speed_y *= -1

			if self.rect.colliderect(player1):
				place_hit = (self.rect.y + ball_size/2) - (player1.rect.y + player_size/2)
				self.speed_x += x_acceleration/10
				self.speed_x *= -1
				self.speed_y = rebound_y/10*(place_hit/(player_size/2))

			elif self.rect.colliderect(player2):
				place_hit = (self.rect.y + ball_size/2) - (player2.rect.y + player_size/2)
				self.speed_x *= -1
				self.speed_x += x_acceleration/10
				self.speed_y = rebound_y/10*(place_hit/(player_size/2))

			self.rect.x += self.speed_x
			self.rect.y += self.speed_y

			if self.rect.top <= 0 or self.rect.bottom >= screen_height:
				self.speed_y *= -1
			if self.rect.left <= 0 or self.rect.right >= screen_width:
				self.speed_x *= -1

		def reset_ball(self):
			self.active = False
			self.speed_x = self.default_speed_x
			self.speed_y = self.default_speed_y
			self.speed_x *= random.choice((-1,1))
			self.speed_y *= random.choice((-1,1))
			self.score_time = pygame.time.get_ticks()
			self.rect.center = (screen_width/2,screen_height/2)
			pygame.mixer.Sound.play(score_sound)

		def restart_counter(self):
			current_time = pygame.time.get_ticks()
			countdown_number = 3

			if current_time - self.score_time <= 700:
				countdown_number = 3
			if 700 < current_time - self.score_time <= 1400:
				countdown_number = 2
			if 1400 < current_time - self.score_time <= 2100:
				countdown_number = 1
			if current_time - self.score_time >= 2100:
				self.active = True

			time_counter = basic_font.render(str(countdown_number),True,accent_color)
			time_counter_rect = time_counter.get_rect(center = (screen_width/2,screen_height/2 + 50))
			pygame.draw.rect(screen,bg_color,time_counter_rect)
			screen.blit(time_counter,time_counter_rect)	

	class GameManager:
		def __init__(self,ball,player1, player2):
			self.player1 = player1
			self.player2 = player2
			self.ball = ball
			self.player1_score = spin_box_variables[2]
			self.player2_score = spin_box_variables[3]
			self.red = (255, 0, 0)

		def run_game(self):
			# Drawing the game objects
			pygame.draw.rect(screen, self.red, self.player1)
			pygame.draw.rect(screen, self.red, self.player2)
			pygame.draw.ellipse(screen, self.red, self.ball)

			# Updating the game objects
			self.player1.update()
			self.player2.update()
			self.ball.update(self.player1, self.player2)
			self.draw_score()
			self.ball_scored_check()

		def draw_score(self):
			player1_score = basic_font.render(str(self.player1_score),True,accent_color)
			player2_score = basic_font.render(str(self.player2_score),True,accent_color)

			player1_score_rect = player1_score.get_rect(midleft = (screen_width / 2 + 40,screen_height/2))
			player2_score_rect = player2_score.get_rect(midright = (screen_width / 2 - 40,screen_height/2))

			screen.blit(player1_score,player1_score_rect)
			screen.blit(player2_score,player2_score_rect)
   
		def ball_scored_check(self):
			if ball.rect.right >= screen_width:
				ball.reset_ball()
				self.player2_score += 1

			elif ball.rect.left <= 0:
				ball.reset_ball()
				self.player1_score += 1
    
			if self.player2_score >= spin_box_variables[1]:
				player2_win_message = basic_font.render("Opponent Wins!!!",True,accent_color)
				player2_win_rect = player2_win_message.get_rect(midright = (screen_width / 2 - 100,screen_height/2))
				screen.blit(player2_win_message, player2_win_rect)
				self.ball.active = False
		
			elif self.player1_score >= spin_box_variables[0]:
				player1_win_message = basic_font.render("Player Wins!!!",True,accent_color)
				player1_win_rect = player1_win_message.get_rect(midright = (screen_width / 2 + 300,screen_height/2))
				screen.blit(player1_win_message, player1_win_rect)
				self.ball.active = False


	# General setup
	pygame.mixer.pre_init(44100,-16,2,512)
	pygame.init()
	clock = pygame.time.Clock()

	# Main Window
	screen_width = 1280
	screen_height = 960
	screen = pygame.display.set_mode((screen_width,screen_height))
	pygame.display.set_caption('Pong')

	# Global Variables
	bg_color = pygame.Color('#2F373F')
	accent_color = (27,35,43)
	basic_font = pygame.font.Font('freesansbold.ttf', 32)
	plob_sound = pygame.mixer.Sound("/Users/kaustubhkarthik/Programs/pyqt_testing/onehand_pong/pong.ogg")
	score_sound = pygame.mixer.Sound("/Users/kaustubhkarthik/Programs/pyqt_testing/onehand_pong/score.ogg")
	middle_strip = pygame.Rect(screen_width/2 - 2,0,4,screen_height)

	# Game objects
	ball = Ball(screen_width / 2 - 15, screen_height / 2 - 15, ball_size, ball_size, ball_speed, ball_speed)
	player1 = Player(screen_width - 20, screen_height / 2 - 70, 10, player_size, player_speed)
	player2 = Player(10, screen_height / 2 - 70, 10, player_size, player_speed)

	game_manager = GameManager(ball, player1, player2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

            # Right Player Movement
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					player1.movement -= player1.speed
				if event.key == pygame.K_DOWN:
					player1.movement += player1.speed
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					player1.movement += player1.speed
				if event.key == pygame.K_DOWN:
					player1.movement -= player1.speed

            # Left Player Movement
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					player2.movement -= player2.speed
				if event.key == pygame.K_s:
					player2.movement += player2.speed
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					player2.movement += player2.speed
				if event.key == pygame.K_s:
					player2.movement -= player2.speed
			
		# Background Stuff
		screen.fill(bg_color)
		pygame.draw.rect(screen,accent_color,middle_strip)
		
		# Run the game
		game_manager.run_game()

		# Rendering
		pygame.display.flip()
		clock.tick(120)

if __name__ == "__main__":
	run()
