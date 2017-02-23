from termcolor import cprint
from random import randint
from pprint import pprint
from time import sleep

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Maze:
	def __init__(self, width, height):
		self.x = 0
		self.y = 0
		self.direction = DOWN
		row = [1] * width
		self.map = []
		for i in range(height):
			self.map.append(row.copy())

		self.paths = [(self.x, self.y)]
		self.visted = set(self.paths)

	def run(self):
		c = 0
		while c < 100:
			c += 1
			if self.direction == DOWN:
				if self.y + 1 < len(self.map):
					if ((self.x, self.y + 1) not in self.visted):
						self.y += 1
						self.visit()
						
				self.direction = randint(0,3)
				continue

			if self.direction == RIGHT:
				if self.x + 1 < len(self.map[self.y]):
					if ((self.x + 1, self.y) not in self.visted):
						self.x += 1
						self.visit()
						
				self.direction = randint(0,3)
				continue

			if self.direction == UP:
				if self.y - 1 >= 0:
					if ((self.x, self.y - 1) not in self.visted):
						self.y -= 1
						self.visit()
						
				self.direction = randint(0,3)
				continue

			if self.direction == LEFT:
				if self.x - 1 >= 0:
					if ((self.x - 1, self.y) not in self.visted):
						self.x -= 1
						self.visit()
						
				self.direction = randint(0,3)
				continue

	def visit(self):
		x, y = self.x, self.y
		self.paths.append((x, y))
		self.visted.add((x, y))

		prev = self.paths[-2]
		deltax = x - prev[0]

		if deltax != 0:
			self.visted.add((prev[0], prev[1] - 1))
			self.visted.add((prev[0], prev[1] + 1))
		else:
			self.visted.add((prev[0] - 1, prev[1]))
			self.visted.add((prev[0] + 1, prev[1]))

	def printpath(self):
		for pos in self.visted:
			x, y = pos
			if x >= 0 and y >= 0:
				self.map[y][x] = 3
		for pos in self.paths:
			x, y = pos
			self.map[y][x] = 4

		cprint(" " * (len(self.map) * 2 + 4), "yellow", "on_yellow")
		for row in self.map:
			cprint("  ", "yellow", "on_yellow", end="")
			for line in row:
				if line == 0:
					print("  ", end="")
				elif line == 1:
					cprint("  ", "white", "on_white", end="")
				elif line == 2:
					print(" H ", end="")
				# else:
				# 	print("   ", end="")
				elif line == 3:
					cprint("  ", "red", "on_red", end="")
				elif line == 4:
					cprint("  ", "grey", "on_blue", end="")
			cprint("  ", "yellow", "on_yellow")
		cprint(" " * (len(self.map) * 2 + 4), "yellow", "on_yellow")

m = Maze(15, 15)
m.run()
m.printpath()
print(m.paths)
# print(m.visted)
