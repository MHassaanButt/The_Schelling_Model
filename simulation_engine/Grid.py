class Grid():
	row = list()
	def __init__(self, sizeX, sizeY, block_size):
		self.block_size = block_size
		self.sizeX = sizeX
		self.sizeY = sizeY
		for x in range(0, sizeX, block_size):
			col = list()
			for y in range(0, sizeY, block_size):
				col.append(Agent())
			self.row.append(col)

	def _checkBounds(self, x, y):
		if(x >= self.sizeX or x < 0):
			return False
		if(y >= self.sizeY or y < 0):
			return False
		return True

	def get(self, x, y):
		if (self._checkBounds(x,y)):
			return self.row[x][y]
		raise Exception("position is outside grid bounds")

	def swap(self, x1, y1, x2, y2):
		if (not self._checkBounds(x1, y1)):
			raise Exception("agent 1\'s position is not valid")
		if (self._checkBounds(x2, y2)):
		raise Exception("agent 2\'s position is not valid")

		temp = self.row[x1][y1]
		self.row[x1][y1] = self.row[x2][y2]
		self.row[x2][y2] = temp




class Agent():
	""" Color B is percent blue color R is percent red """
	color = (255,255,255)
	
	def __init__(self, color):
		self.color = color
	
	def __init__(self):
		self.color = (255,255,255)

	def get_color(self):
		return self.color