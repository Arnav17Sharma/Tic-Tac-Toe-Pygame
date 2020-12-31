import pygame

pygame.init()
size = (600, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('TIC-TAC-TOE')
font = pygame.font.SysFont(None, 24)


text = 'O'
running = True
MOVES = 0
moves_lst = []
lst = []
result_dict = {}


def check_results(result_dict):
	global running
	start = (0,0)
	end=(600,600)
	if len(result_dict)>=5:
		try:
			if result_dict[0]==result_dict[1]==result_dict[2]:  
				print(result_dict[0],'WON!!')
				# screen.fill((0,0,0))
				# img = font.render(f'{result_dict[0]} Won!')
				# screen.blit(img, (300,700))
				# pygame.draw.line(screen, (255, 0, 0), start, end)
				running = False
				print(f'{running} HAI RUNNING!!!')
				return running, result_dict[0]

		except:pass
		try:
			if result_dict[3]==result_dict[4]==result_dict[5]:
				print(result_dict[3],'WON!!')
				# screen.fill((0,0,0))
				# img = font.render(f'{result_dict[3]} Won!')
				# screen.blit(img, (300,700))
				# pygame.draw.line(screen, (255, 0, 0), start, end)
				running = False
				return running, result_dict[3]
				
		except:pass
		try:
			if result_dict[6]==result_dict[7]==result_dict[8]:
				print(result_dict[6],'WON!!')
				# screen.fill((0,0,0))
				# img = font.render(f'{result_dict[6]} Won!')
				# screen.blit(img, (300,700))
				# pygame.draw.line(screen, (255, 0, 0), start, end)
				running = False
				return running, result_dict[6]
				
		except:pass
		try:
			if result_dict[0]==result_dict[3]==result_dict[6]:
				print(result_dict[0],'WON!!')
				# screen.fill((0,0,0))
				# img = font.render(f'{result_dict[0]} Won!')
				# screen.blit(img, (300,700))
				# pygame.draw.line(screen, (255, 0, 0), start, end)
				running = False
				return running, result_dict[0]
				
		except:pass
		try:
			if result_dict[1]==result_dict[4]==result_dict[7]:
				print(result_dict[1],'WON!!')
				# screen.fill((0,0,0))
				# img = font.render(f'{result_dict[1]} Won!')
				# screen.blit(img, (300,700))
				# pygame.draw.line(screen, (255, 0, 0), start, end)
				running = False
				return running, result_dict[1]
				
		except:pass
		try:
			if result_dict[2]==result_dict[5]==result_dict[8]:
				print(result_dict[2],'WON!!')
				# screen.fill((0,0,0))
				# img = font.render(f'{result_dict[2]} Won!')
				# screen.blit(img, (300,700))
				# pygame.draw.line(screen, (255, 0, 0), start, end)
				running = False
				return running, result_dict[2]
				
		except:pass
		try:
			if result_dict[0]==result_dict[4]==result_dict[8]:
				print(result_dict[0],'WON!!')
				# screen.fill((0,0,0))
				# img = font.render(f'{result_dict[0]} Won!')
				# screen.blit(img, (300,700))
				# pygame.draw.line(screen, (255, 0, 0), start, end)
				running = False
				return running, result_dict[0]
				
		except:pass
		try:
			if result_dict[2]==result_dict[4]==result_dict[6]:
				print(result_dict[2],'WON!!')
				# screen.fill((0,0,0))
				# img = font.render(f'{result_dict[2]} Won!')
				# screen.blit(img, (300,700))
				# pygame.draw.line(screen, (255, 0, 0), start, end)
				running = False
				return running, result_dict[2]
		except:pass
		pygame.display.update()
	return running, None

def make_board(move_lst):
	for i in range(3):
		for j in range(3):
			lst.append([(j*200), (i*200)])
			rect = pygame.Rect((j*200), (i*200), 200, 200)
			pygame.draw.rect(screen, (255, 255, 0), rect)
			pygame.draw.rect(screen, (0, 0, 0), rect, 3)
	for move in moves_lst:
		# global text
		img1 = font.render(move[0], True, (255, 0, 0))
		screen.blit(img1, move[1])
	pygame.display.update()
	return running


def move(text, el):
	moves_lst.append([text, (el[0]+80, el[1]+100)])


def check_text(text):
	print(f"GOT {text}")
	if text=='X':
		print("IDHAR NHI AANA!")
		text='O'
	else:
		print("IDHAR AANA BE!")
		text='X'
	return text

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = 0

		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_position = pygame.mouse.get_pos()
			print(mouse_position)
			for el in lst:
				if el[0]<mouse_position[0]<el[0]+200 and el[1]<mouse_position[1]<el[1]+200:
					text = check_text(text)
					move(text, el)
					result_dict[lst.index(el)] = text
					break

	make_board(moves_lst)
	running, winner = check_results(result_dict)
	print(running)
	pygame.display.update()
	if not running:

		screen1 = pygame.display.set_mode((300,300))
		pygame.display.set_caption('RESULTS')
		showing = 1
		while showing:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					showing = False
			img = font.render(f'{winner} Won!', True, (255, 0, 0))
			screen1.blit(img, (120,150))
			pygame.display.update()
		pygame.quit()
# print(lst[-9:])
# print(result_dict)
pygame.quit()