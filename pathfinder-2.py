from pprint import pprint
from termcolor import cprint

map_ = """\
000000000000000
000000000000000
000111111100000
000000010000000
000000010000000
000000000000010
000111000000010
000100000001110
000100000000000"""

def parse_map(map_):
	res = []
	for col in map_.split("\n"):
		res.append([])
		for row in col:
			res[-1].append(int(row))
	return res

class Map:
	def __init__(self, map_):
		self.map = map_
		self.filled = set()

	def print(self):
			cprint(" " * (len(self.map[0]) * 2 + 4), "yellow", "on_yellow")
			for col in self.map:
				cprint("  ", "yellow", "on_yellow", end="")
				for row in col:
					if row == 0:
						print(". ", end="")
					elif row == 1:
						cprint("  ", "white", "on_white", end="")
					elif row == 2:
						cprint("  ", "blue", "on_blue", end="")
					elif row == 3:
						cprint("  ", "red", "on_red", end="")
				cprint("  ", "yellow", "on_yellow")
			cprint(" " * (len(self.map[0]) * 2 + 4), "yellow", "on_yellow")

	def fill_up(self):
		for y, col in enumerate(self.map):
			for x, pos in enumerate(col):
				if pos == 1 and (x, y) not in self.filled:
					self.filled.add((x, y))

					self.thought_box(x, y, col)

	def thought_box(self, x, y, col):
		self.map[y][x] = 3
		for i in range(x + 1, len(col)):
			if self.map[y][i] == 1:
				self.filled.add((i, y))
			if y + 1 < len(self.map):
				if self.map[y + 1][i] == 1:
					for e in range(y + 1, len(self.map)):
						if self.map[e][i] == 1:
							self.filled.add((i, e))
							for tx in range(x, i):
								self.map[e][tx] = 2
								self.filled.add((tx, e))
						else:
							break
					break
				elif self.map[y][i] == 0:
					break

			# if y - 1 >= 0:
			# 	if self.map[y - 1][i] == 1 and (i, y - 1) not in self.filled:
			# 		for e in range(0, y):
			# 			if self.map[e][i] == 1:
			# 				for tx in range(x, i):
			# 					self.map[e][tx] = 2
			# 					self.filled.add((tx, e))
			# 		break
		if y + 1 < len(self.map):
			if self.map[y + 1][x] == 1 and (x, y + 1) not in self.filled:
				for e in range(y + 1, len(self.map)):
					if self.map[e][x] == 1:
						self.filled.add((x, e))
						for i in range(x + 1, len(col)):
							if self.map[y][i] == 1:
								self.map[e][i] = 2
								self.filled.add((i, e))
							else:
								break
					else:
						break

		# if y + 1 < len(self.map):
		# 	if self.map[y + 1][x] == 1 and (x, y + 1) not in self.filled:
		# 		for e in range(y + 1, len(self.map)):
		# 			if self.map[e][x] == 1:
		# 				for i in range(x + 1, len(col)):
		# 					if self.map[y][i] == 1:
		# 						self.map[e][i] = 2
		# 						self.filled.add((i, e))


if __name__ == "__main__":
	map_ = parse_map(map_)
	m = Map(map_)
	m.fill_up()
	m.print()