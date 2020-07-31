#https://realpython.com/pygame-a-primer/
# Simple pygame program

#pygame.mixer.music :pygame module for controlling streamed audio
# Import and initialize the pygame library
import pygame, datetime
pygame.init()
def play_sound():
	print("Test play music")
	pygame.mixer.init()
	pygame.mixer.music.load("HaiViSaoLac-TruongVu_3d7e9.mp3")
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
schedule_time = "20200731_093500"
alarm_setting_text = smallfont.render(schedule_time , True , white)

#this test for alarm
current = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
text2 = bigfont.render(current, True, green, blue)
textRect = text2.get_rect()  # text surface object 
textRect.center = (width // 2, height // 2)   # set the center of the rectangular object. 


Clock = pygame.time.Clock()
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) # fired once every second

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
			
		if event.type == CLOCKTICK:
			current = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
			text2 = bigfont.render(current, True, green, blue)
			screen.blit(text2, textRect)  #draw one image onto another
			textRect.center = (width // 2, height // 2)
			
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
	pygame.display.flip()
	
# Done! Time to quit.
pygame.quit()

