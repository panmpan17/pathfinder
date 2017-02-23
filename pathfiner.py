from termcolor import cprint

UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"

class Map:
	def __init__(self, map_=[]):
		if len(map_) == 0:
			map_ = [
				[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,1,1,0],
				[0,0,1,0,0],
				[0,0,1,0,0],
				[0,0,1,0,2],
			]
		self.map = map_

	def find_path(self, pos):
		self.x, self.y = pos
		self.paths = [(self.x, self.y)]

		self.dead_end = set()
		self.paths_tested = set(self.paths)
		self.direction = DOWN

		while self.map[self.y][self.x] != 2:
			if self.direction == DOWN:
				if self.y + 1 < len(self.map):
					if ((self.map[self.y + 1][self.x] != 1) and
							((self.x, self.y + 1) not in self.dead_end)):
						self.y += 1
						self.paths.append((self.x, self.y))
						self.paths_tested.add((self.x, self.y))
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
						self.paths_tested.add((self.x, self.y))
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
						self.paths_tested.add((self.x, self.y))
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
						self.paths_tested.add((self.x, self.y))
						continue
				turn = self.turnupdown()
				if turn:
					continue

				rev = self.paths.copy()
				rev.reverse()

				self.backward(rev)

	def turnupdown(self):
		if self.y - 1 >= 0:
			if (self.map[self.y - 1][self.x] != 1 and
					((self.x, self.y - 1) not in self.paths)):
				self.direction = UP
				return True
		if self.y + 1 < len(self.map):
			if (self.map[self.y + 1][self.x] != 1 and
					((self.x, self.y + 1) not in self.paths)):
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
						return

			if rx + 1 < len(self.map[ry]):
				if self.map[ry][rx + 1] != 1:
					res = self.checknexpre(rev, i, rx + 1, ry)
					if res:
						self.paths = self.paths[:self.paths.index((rx, ry)) + 1]
						self.x, self.y = rx, ry
						self.direction = RIGHT
						return

			if ry - 1 >= 0:
				if self.map[ry -1][rx] != 1:
					res = self.checknexpre(rev, i, rx, ry - 1)
					if res:
						self.paths = self.paths[:self.paths.index((rx, ry)) + 1]
						self.x, self.y = rx, ry
						self.direction = UP
						return

			if ry + 1 < len(self.map):
				if self.map[ry + 1][rx] != 1:
					res = self.checknexpre(rev, i, rx, ry + 1)
					if res:
						self.paths = self.paths[:self.paths.index((rx, ry)) + 1]
						self.x, self.y = rx, ry
						self.direction = DOWN
						return
			self.dead_end.add((rx, ry))

	def checknexpre(self, l, i, x, y):
		return (x, y) not in self.paths_tested

	def printpath(self):
		for pos in self.dead_end:
			x, y = pos
			self.map[y][x] = 4
		for pos in self.paths:
			x, y = pos
			self.map[y][x] = 3

		cprint(" " * (len(self.map) * 2 + 4), "yellow", "on_yellow")
		for row in self.map:
			cprint("  ", "yellow", "on_yellow", end="")
			for line in row:
				if line == 0:
					print("  ", end="")
				elif line == 1:
					cprint("  ", "white", "on_white", end="")
				elif line == 2:
					print(" H", end="")
				# else:
				# 	print("   ", end="")
				elif line == 3:
					cprint("  ", "red", "on_red", end="")
				elif line == 4:
					cprint("  ", "grey", "on_blue", end="")
			cprint("  ", "yellow", "on_yellow")
		cprint(" " * (len(self.map) * 2 + 4), "yellow", "on_yellow")

if __name__ == "__main__":
	m = Map()
	try:
		m.find_path((0, 0))
	except KeyboardInterrupt:
		pass
	m.printpath()