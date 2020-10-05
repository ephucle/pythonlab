#https://realpython.com/pygame-a-primer/
# Simple pygame program

#pygame.mixer.music :pygame module for controlling streamed audio
# Import and initialize the pygame library
import pygame, datetime
pygame.init()
def play_sound():
	print("Test play music")
	pygame.mixer.init()
	#pygame.mixer.music.load("HaiViSaoLac-TruongVu_3d7e9.mp3")
	pygame.mixer.music.load("hvsl.mp3")
	print("Start to play music")
	pygame.mixer.music.play()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# white color 
white = (255,255,255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
purple = (102, 0, 102)
lightblue= (0, 0, 255)
# light shade of the button 
color_light = (170,170,170) 

# dark shade of the button 
color_dark = (100,100,100) 

# stores the width of the 
# screen into a variable 
width = screen.get_width() 

# stores the height of the 
# screen into a variable 
height = screen.get_height()

# defining a font 
smallfont = pygame.font.SysFont('freesansbold.ttf',30)
bigfont = pygame.font.SysFont('freesansbold.ttf',50)

# rendering a text written in 
# this font 


text_play = smallfont.render('Play' , True , white)
text_stop = smallfont.render('Stop Music' , True , white)
#schedule_time = "20200731_093500"
schedule_time = "20201005 093730"
print("schedule_time", schedule_time)
alarm_setting_text = smallfont.render(schedule_time , True , white)

#this test for alarm
current = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
text2 = bigfont.render(current, True, green, blue)
textRect = text2.get_rect()  # text surface object 
textRect.center = (width // 2 + 50, height // 2)   # set the center of the rectangular object. 


Clock = pygame.time.Clock()
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) # fired once every second


input_box = pygame.Rect(150, 100, 190, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''


# Run until the user asks to quit
running = True
while running:
	# Did the user click the window close button?
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	#checks if a mouse is clicked 
		if event.type == pygame.MOUSEBUTTONDOWN: 
			#if the mouse is clicked on the 
			# button the game is terminated 
			if 0 <= mouse[0] <= 200 and height -200 <= mouse[1] <= height: 
				play_sound()
			
			if 0 <= mouse[0] <= 140 and 0 <= mouse[1] <= 140: 
				print("stop music")
				pygame.mixer.music.stop()
			# If the user clicked on the input_box rect.
			if input_box.collidepoint(event.pos):
				# Toggle the active variable.
				active = not active
			else:
				active = False
				# Change the current color of the input box.
			color = color_active if active else color_inactive
		if event.type == pygame.KEYDOWN:
			if active:
				if event.key == pygame.K_RETURN:
					print(text)
					text = ''
				elif event.key == pygame.K_BACKSPACE:
					text = text[:-1]
				else:
					text += event.unicode
		if event.type == CLOCKTICK:
			current = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
			text2 = bigfont.render(current, True, green, blue)
			screen.blit(text2, textRect)  #draw one image onto another
			
			
			#neu cung thoi gian thi play sound
			if current == schedule_time:
				play_sound()
			
	# Fill the background with white
	screen.fill(white)
	
	# copying the text surface object 
	# to the display surface object  
	# at the center coordinate. 
	screen.blit(text2, textRect) 
	
	# stores the (x,y) coordinates into 
	# the variable as a tuple 
	mouse = pygame.mouse.get_pos() 
	
	# if mouse is hovered on a button it 
	# changes to lighter shade 
	##add another button, cho chuc nang doi mau neu chuot di chuyen qua no
	if 0 <= mouse[0] <= 140 and height - 140 <= mouse[1] <= height: 
		pygame.draw.rect(screen,lightblue,[0,height - 200,200,height]) 
	else: 
		pygame.draw.rect(screen,purple,[0,height - 200,200,height]) 
	
	#add another button, cho chuc nang doi mau neu chuot di chuyen qua no
	if 0 <= mouse[0] <= 140 and 0 <= mouse[1] <= 140: 
		pygame.draw.rect(screen,green,[0,0,140,140]) 
	else: 
		pygame.draw.rect(screen,blue,[0,0,140,140]) 
	
	# superimposing the text onto our button 
	screen.blit(text_play , (0,height-140 + 10)) 
	screen.blit(alarm_setting_text , (0, height-140+ 50)) 
	screen.blit(text_stop , (0+10,0)) 

	# Flip the display
	
	# Render the current text.
	#txt_surface = font.render(text, True, color)
	txt_surface = smallfont.render(text, True, color)
	
	# Resize the box if the text is too long.
	width = max(200, txt_surface.get_width()+10)
	input_box.w = width
	# Blit the text.
	screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
	# Blit the input_box rect.
	pygame.draw.rect(screen, color, input_box, 2)
	
	pygame.display.flip()
	
# Done! Time to quit.
pygame.quit()

