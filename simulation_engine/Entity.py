import random
class Grid():
	row = list()
	free = list()
	unhappy = list()
	def __init__(self, sizeX, sizeY, block_size, func=None, percent_free=.10, threshold_for_red = 25, happiness_threshold = .75):
		self.block_size = block_size
		self.sizeX = int(sizeX/block_size)
		self.sizeY = int(sizeY/block_size)
		self.happiness_threshold = happiness_threshold
		for x in range(0, sizeX, block_size):
			col = list()
			for y in range(0, sizeY, block_size):
				color = self.generate_color(func, percent_free)
				agent = Agent(color, threshold_for_red)
				col.append(agent)
				if(color == (255,255,255)):
					self.free.append((int(x/block_size),int(y/block_size)))
			self.row.append(col)
		#print(self.free)

	def _checkBounds(self, pos):
		x = pos[0]
		y = pos[1]
		if(x >= self.sizeX or x < 0):
			return False
		if(y >= self.sizeY or y < 0):
			return False
		return True

	def get(self, pos):
		x = pos[0]
		y = pos[1]
		if (self._checkBounds((x,y))):
			return self.row[x][y]
		return None

	def swap_free_space(self, main):
		self._checkBounds(main)

		x1 = main[0]
		y1 = main[1]
		index = random.choice(range(len(self.free)))
		free_space = self.free[index]
		x2 = free_space[0]
		y2 = free_space[1]

		#print("agent @ ",x1,y1, "is not happy; moving them to",x2,y2)
		self.free[index] = (x1, y1)
		temp = self.row[x1][y1]
		self.row[x1][y1] = self.row[x2][y2]
		self.row[x2][y2] = temp
		
		#print(self.free)

	def move_unhappy(self):
		while(len(self.unhappy) > 0):
			index = random.choice(range(len(self.unhappy)))
			self.swap_free_space(self.unhappy[index])
			del self.unhappy[index]

	def get_unhappy(self):
		for x in range(0, self.sizeX):
			for y in range(0, self.sizeY):
				pos = (x,y)
				if(not self.is_agent_happy(pos)):
					self.unhappy.append(pos)

		return len(self.unhappy)


	def generate_color(self, func=None, percent_free=.10):
		if(random.random() < percent_free):
			return (255,255,255)
		if (func is None):
			b = random.randrange(0,255,1)
			r = 255-b
			g = 255
			return (r,b,g)
		return (0,0,0) #place holder func should return a color similar to above

	def is_agent_happy(self, pos):
		happy_with_percent = self.get_happiness_with_neighbors(pos)
		
		if( happy_with_percent  < self.happiness_threshold):
			#print(pos,happy_with_percent )
			return False 
		return True 

	def is_agent_free(self, pos):
		if(self.get(pos).race == "F"):
			return True

	def get_happiness_with_neighbors(self, pos):
		x = pos[0]
		y = pos[1]
		neighbors = ((x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1), (x - 1, y + 1), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1))
		main_agent = self.get(pos)
		happy = 0
		total = 0
		for neighbor in neighbors:
			neighbor_agent = self.get(neighbor)
			
			if(neighbor_agent == None):
				continue
			total += 1
			if(self.is_agent_free(pos) or self.is_piece_happy_with_neighbor(main_agent, neighbor_agent)):
				happy += 1
			

		return float(happy/total)


	def is_piece_happy_with_neighbor(self, main, n):
		return main.race == n.race or n.race == 'F' 



class Agent():
	""" Color B is percent blue color R is percent red , threshhold for similarity is what color is considereted \"red\""""
	color = (255,255,255)
	preference_color = (0,0,0)
	
	def __init__(self, color, threshold_for_red=127):
		self.color = color
		self.race = "R" if (color[0]>=threshold_for_red) else "B"
		if(color == (255,255,255)):
			self.race = "F"

	def get_color(self):
		return self.color

	def set_color(self):
		return self.color


