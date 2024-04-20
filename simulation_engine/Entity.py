import random
class Grid():
	row = list()
	def __init__(self, sizeX, sizeY, block_size, func=None, percent_free=.10, threshold_for_red = 127):
		self.block_size = block_size
		self.sizeX = sizeX
		self.sizeY = sizeY
		for x in range(0, sizeX, block_size):
			col = list()
			for y in range(0, sizeY, block_size):
				col.append(Agent(self.generate_color(func, percent_free), threshold_for_red))
			self.row.append(col)

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
		raise Exception("position is outside grid bounds")

	def swap(self, main, n):
		self._checkBounds(main)
		self._checkBounds(n)
		x1 = main[0]
		y1 = main[1]
		x2 = n[0]
		y2 = n[1]

		temp = self.row[x1][y1]
		self.row[x1][y1] = self.row[x2][y2]
		self.row[x2][y2] = temp

	def generate_color(self, func=None, percent_free=.10):
		if(random.random() < percent_free):
			return (255,255,255)
		if (func is None):
			b = random.randrange(0,255,1)
			r = 255-b
			g = 255
			return (r,b,g)
		return (0,0,0) #place holder func should return a color similar to above

	def is_piece_happy_with_neighbor(self, main, n):
		agentMain = self.get(main)
		agentN = self.get(n)
		return agentMain.race == agentN.race

	def find_free_space(self):
		for x in range(len(self.row)):
			for y in range(len(self.row[0])):
				agent = self.get((x,y))
				if(agent.race == "F"):
					return (x,y)



class Agent():
	""" Color B is percent blue color R is percent red , threshhold for similarity is what color is considereted \"red\""""
	color = (255,255,255)
	preference_color = (0,0,0)
	race = "F"
	
	def __init__(self, color, threshold_for_red=127):
		self.color = color
		self.race = "R" if (color[0]>=threshold_for_red) else "B"
		if(color == (255,255,255)):
			self.race = "F"

	def get_color(self):
		return self.color

	def set_color(self):
		return self.color

