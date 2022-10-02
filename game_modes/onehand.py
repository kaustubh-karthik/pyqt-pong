def run(slider_variables, spin_box_variables):
	import pygame, sys, random
	from extras import hand_coords
	sys.path.insert(0, '/Users/kaustubhkarthik/Programs/pyqt_testing/onehand_pong/hand_coords.py')

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
			self.hand_control()
			self.screen_constrain()
   
		def hand_control(self):
			hand_landmarks = hand_coords.get_hand_landmarks()
			if hand_landmarks:
				for landmark in hand_landmarks:
						pygame.draw.circle(screen, (255, 0, 255), (landmark[0], landmark[1]), 5)
						
				index_finger = hand_landmarks[8]
				self.rect.y = index_finger[1]

	class Ball(Block):
		def __init__(self, x_pos, y_pos, width, height, speed_x, speed_y):
			super().__init__(x_pos, y_pos, width, height)
			self.default_speed_x = speed_x * 4
			self.default_speed_y = speed_y * 4
			self.speed_x = speed_x * random.choice((-1,1)) * 4
			self.speed_y = speed_y * random.choice((-1,1)) * 4
			self.active = False
			self.score_time = 0
    
		def update(self, player, opponent):
			if self.active:
				self.rect.x += self.speed_x
				self.rect.y += self.speed_y
				self.collisions(player, opponent)
			else:
				self.restart_counter()
			
		def collisions(self, player, opponent):
			if self.rect.top <= 0 or self.rect.bottom >= screen_height:
				pygame.mixer.Sound.play(plob_sound)
				self.speed_y *= -1

			if self.rect.colliderect(player):
				place_hit = (self.rect.y + ball_size/2) - (player.rect.y + player_size/2)
				self.speed_x += x_acceleration/10
				self.speed_x *= -1
				self.speed_y = (rebound_y/10)*(place_hit/(player_size))

			elif self.rect.colliderect(opponent):
				place_hit = (self.rect.y + ball_size/2) - (opponent.rect.y + player_size/2)
				self.speed_x *= -1
				self.speed_x += x_acceleration/10
				self.speed_y = (rebound_y/10)*(place_hit/(player_size/2))

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

	class Opponent(Block):
		def __init__(self, x_pos, y_pos, width, height, speed):
			super().__init__(x_pos,y_pos, width, height)
			self.speed = speed
   
		def update(self,ball):
			if self.rect.top < ball.rect.y:
				self.rect.y += self.speed
			if self.rect.bottom > ball.rect.y:
				self.rect.y -= self.speed
			self.screen_constrain()

		def screen_constrain(self):
			if self.rect.top <= 0:
				self.rect.top = 0
			if self.rect.bottom >= screen_height:
				self.rect.bottom = screen_height		

	class GameManager:
		def __init__(self,ball,player, opponent):
			self.player = player
			self.opponent = opponent
			self.ball = ball
			self.player_score = spin_box_variables[2]
			self.opponent_score = spin_box_variables[3]
			self.red = (255, 0, 0)

		def run_game(self):
			# Drawing the game objects
			pygame.draw.rect(screen, self.red, self.player)
			pygame.draw.rect(screen, self.red, self.opponent)
			pygame.draw.ellipse(screen, self.red, self.ball)

			# Updating the game objects
			self.player.update()
			self.opponent.update(self.ball)
			self.ball.update(self.player, self.opponent)
			self.draw_score()
			self.ball_scored_check()

		def draw_score(self):
			player_score = basic_font.render(str(self.player_score),True,accent_color)
			opponent_score = basic_font.render(str(self.opponent_score),True,accent_color)

			player_score_rect = player_score.get_rect(midleft = (screen_width / 2 + 40,screen_height/2))
			opponent_score_rect = opponent_score.get_rect(midright = (screen_width / 2 - 40,screen_height/2))

			screen.blit(player_score,player_score_rect)
			screen.blit(opponent_score,opponent_score_rect)
   
		def ball_scored_check(self):
			if ball.rect.right >= screen_width:
				ball.reset_ball()
				self.opponent_score += 1

			elif ball.rect.left <= 0:
				ball.reset_ball()
				self.player_score += 1
    
			if self.opponent_score >= spin_box_variables[1]:
				opponent_win_message = basic_font.render("Opponent Wins!!!",True,accent_color)
				opponent_win_rect = opponent_win_message.get_rect(midright = (screen_width / 2 - 100,screen_height/2))
				screen.blit(opponent_win_message, opponent_win_rect)
				self.ball.active = False
		
			elif self.player_score >= spin_box_variables[0]:
				player_win_message = basic_font.render("Player Wins!!!",True,accent_color)
				player_win_rect = player_win_message.get_rect(midright = (screen_width / 2 + 300,screen_height/2))
				screen.blit(player_win_message, player_win_rect)
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
	plob_sound = pygame.mixer.Sound("/Users/kaustubhkarthik/Programs/pyqt_testing/extras/pong.ogg")
	score_sound = pygame.mixer.Sound("/Users/kaustubhkarthik/Programs/pyqt_testing/extras/score.ogg")
	middle_strip = pygame.Rect(screen_width/2 - 2,0,4,screen_height)

	# Game objects
	ball = Ball(screen_width / 2 - 15, screen_height / 2 - 15, ball_size, ball_size, ball_speed, ball_speed)
	player = Player(screen_width - 20, screen_height / 2 - 70, 10, player_size, player_speed)
	opponent = Opponent(10, screen_height / 2 - 70, 10, player_size, player_speed * 4)

	game_manager = GameManager(ball, player, opponent) 

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		# Background Stuff
		screen.fill(bg_color)
		pygame.draw.rect(screen,accent_color,middle_strip)
		
		# Run the game
		game_manager.run_game()

		# Rendering
		pygame.display.flip()
		clock.tick(30)

if __name__ == "__main__":
	run()
