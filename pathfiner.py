from pprint import pprint

UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"


class Map:
	def __init__(self, map_=[]):
		if len(map_) == 0:
			map_ = [
				[0,0,0,1,0,0,0,0,1,0],
				[0,1,0,1,0,0,1,0,1,0],
				[0,1,0,0,0,0,0,0,0,0],
				[0,1,1,1,1,1,1,1,1,0],
				[0,1,0,0,0,0,0,0,0,0],
				[0,1,1,1,1,1,1,0,1,1],
				[0,0,0,1,0,0,1,0,0,0],
				[0,0,0,1,1,0,1,1,1,0],
				[0,0,0,0,0,0,1,0,1,0],
				[0,0,0,1,1,1,1,0,0,2],
			]
		self.map = map_

	def find_path(self, pos):
		self.x, self.y = pos
		self.paths = [(self.x, self.y)]

		self.dead_end = set()
		# self.paths_tested = {}
		self.direction = DOWN

		while self.map[self.y][self.x] != 2:
			if len(self.paths) > 50:
				break
			if self.direction == DOWN:
				if self.y + 1 < len(self.map):
					if ((self.map[self.y + 1][self.x] != 1) and
							((self.x, self.y + 1) not in self.dead_end)):
						self.y += 1
						self.paths.append((self.x, self.y))
						continue
				turn = self.turnleftright()
				if turn:
					continue

				rev = self.paths.copy()
				rev.reverse()

				self.backward(rev)

			if self.direction == RIGHT:
				if self.x + 1 < len(self.map[self.y]):
					if ((self.map[self.y][self.x + 1] != 1) and
							((self.x + 1, self.y) not in self.dead_end)):
						self.x += 1
						self.paths.append((self.x, self.y))
						continue
				turn = self.turnupdown()
				if turn:
					continue

				rev = self.paths.copy()
				rev.reverse()

				self.backward(rev)

			if self.direction == UP:
				if self.y - 1 >= 0:
					if ((self.map[self.y - 1][self.x] != 1) and
							((self.x, self.y - 1) not in self.dead_end)):
						self.y -= 1
						self.paths.append((self.x, self.y))
						continue
				turn = self.turnleftright()
				if turn:
					continue

				rev = self.paths.copy()
				rev.reverse()

				self.backward(rev)

			if self.direction == LEFT:
				if self.x - 1 >= 0:
					if ((self.map[self.y][self.x - 1] != 1) and
							((self.x - 1, self.y) not in self.dead_end)):
						self.x -= 1
						self.paths.append((self.x, self.y))
						continue
				turn = self.turnupdown()
				if turn:
					continue

				rev = self.paths.copy()
				rev.reverse()

				self.backward(rev)

	def turnupdown(self):
		if self.y - 1 >= 0:
			if self.map[self.y - 1][self.x] != 1 and
					((self.x, self.y - 1) not in self.paths):
				self.direction = UP
				return True
		if self.y + 1 < len(self.map):
			if self.map[self.y + 1][self.x] != 1 and
					((self.x, self.y + 1) not in self.paths):
				self.direction = DOWN
				return True
		return False

	def turnleftright(self):
		if self.x - 1 >= 0:
			if (self.map[self.y][self.x - 1] != 1 and
					((self.x - 1, self.y) not in self.paths)):
				self.direction = LEFT
				return True
		if self.x + 1 < len(self.map[self.y]):
			if (self.map[self.y][self.x + 1] != 1 and
					((self.x + 1, self.y) not in self.paths)):
				self.direction = RIGHT
				return True
		return False

	def backward(self, rev):
		for i, p in enumerate(rev):
			rx, ry = p
			if rx - 1 >= 0:
				if self.map[ry][rx - 1] != 1:
					res = self.checknexpre(rev, i, rx - 1, ry)
					if res:
						self.paths = self.paths[:self.paths.index((rx, ry)) + 1]
						self.x, self.y = rx, ry
						self.direction = LEFT
						break

			if rx + 1 < len(self.map[ry]):
				if self.map[ry][rx + 1] != 1:
					res = self.checknexpre(rev, i, rx + 1, ry)
					if res:
						self.paths = self.paths[:self.paths.index((rx, ry)) + 1]
						self.x, self.y = rx, ry
						self.direction = RIGHT
						break

			if ry - 1 >= 0:
				if self.map[ry -1][rx] != 1:
					res = self.checknexpre(rev, i, rx, ry - 1)
					if res:
						self.paths = self.paths[:self.paths.index((rx, ry)) + 1]
						self.x, self.y = rx, ry
						self.direction = UP
						break

			if ry + 1 < len(self.map):
				if self.map[ry + 1][rx] != 1:
					res = self.checknexpre(rev, i, rx, ry + 1)
					if res:
						self.paths = self.paths[:self.paths.index((rx, ry)) + 1]
						self.x, self.y = rx, ry
						self.direction = DOWN
						break
			self.dead_end.add((rx, ry))

	def checknexpre(self, l, i, x, y):
		next_ = None
		prev = None

		try:
			next_ = l[i - 1]
		except:
			pass
		try:
			prev = l[i + 1]
		except:
			pass

		if (((x, y) != next_) and ((x, y) != prev)):
			return True
		return False

	def printpath(self):
		for pos in self.dead_end:
			x, y = pos
			self.map[y][x] = 4
		for pos in self.paths:
			x, y = pos
			self.map[y][x] = 3
		pprint(self.map)
		print("-" * (len(self.map) * 3 + 2))
		for row in self.map:
			print("|", end="")
			for line in row:
				if line == 0:
					print("   ", end="")
				elif line == 1:
					print(" O ", end="")
				elif line == 3:
					print(" + ", end="")
				elif line == 4:
					print(" X ", end="")
			print("|")
		print("-" * (len(self.map) * 3 + 2))

if __name__ == "__main__":
	m = Map()
	m.find_path((0, 0))
	m.printpath()
	print(m.paths)