from pprint import pprint

UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"

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

x = 0
y = 0

paths = [(x, y)]
direction = DOWN
paths_tested = {}
dead_end = set()

def printpath(p):
	for pos in dead_end:
		x, y = pos
		map_[y][x] = 4
	for pos in p:
		x, y = pos
		map_[y][x] = 3
	pprint(map_)
	print("-" * (len(map_) * 3 + 2))
	for row in map_:
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
	print("-" * (len(map_) * 3 + 2))

def checknexpre(l, i, x, y):
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

try:
	while map_[y][x] != 2:
		if len(paths) > 50:
			break
		if direction == DOWN:
			if y + 1 < len(map_):
				if ((map_[y + 1][x] != 1) and ((x, y + 1) not in dead_end)):
					y += 1
					paths.append((x, y))
					continue
			if x - 1 >= 0:
				if map_[y][x - 1] != 1 and ((x - 1, y) not in paths):
					direction = LEFT
					continue
			if x + 1 < len(map_[y]):
				if map_[y][x + 1] != 1 and ((x + 1, y) not in paths):
					direction = RIGHT
					continue

			rev = paths.copy()
			rev.reverse()

			for i, p in enumerate(rev):
				rx, ry = p
				if rx - 1 >= 0:
					if map_[ry][rx - 1] != 1:
						res = checknexpre(rev, i, rx-1, ry)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = LEFT
							break

				if rx + 1 < len(map_[ry]):
					if map_[ry][rx + 1] != 1:
						res = checknexpre(rev, i, rx+1, ry)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = RIGHT
							break

				if ry - 1 >= 0:
					if map_[ry -1][rx] != 1:
						res = checknexpre(rev, i, rx, ry-1)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = UP
							break

				if ry + 1 < len(map_):
					if map_[ry + 1][rx] != 1:
						res = checknexpre(rev, i, rx, ry+1)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = DOWN
							break

				dead_end.add((rx, ry))

		if direction == RIGHT:
			if x + 1 < len(map_[y]):
				if ((map_[y][x + 1] != 1) and ((x + 1, y) not in dead_end)):
					x += 1
					paths.append((x, y))
					continue
			if y - 1 >= 0:
				if map_[y - 1][x] != 1 and ((x, y - 1) not in paths):
					direction = UP
					continue
			if y + 1 < len(map_):
				if map_[y + 1][x] != 1 and ((x, y + 1) not in paths):
					direction = DOWN
					continue

			rev = paths.copy()
			rev.reverse()

			for i, p in enumerate(rev):
				
				if rx - 1 >= 0:
					if map_[ry][rx - 1] != 1:
						res = checknexpre(rev, i, rx-1, ry)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = LEFT
							break

				if rx + 1 < len(map_[ry]):
					if map_[ry][rx + 1] != 1:
						res = checknexpre(rev, i, rx+1, ry)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = RIGHT
							break

				if ry - 1 >= 0:
					if map_[ry -1][rx] != 1:
						res = checknexpre(rev, i, rx, ry-1)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = UP
							break

				if ry + 1 < len(map_):
					if map_[ry + 1][rx] != 1:
						res = checknexpre(rev, i, rx, ry+1)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = DOWN
							break

				dead_end.add((rx, ry))

		if direction == UP:
			if y - 1 >= 0:
				if ((map_[y - 1][x] != 1) and ((x, y - 1) not in dead_end)):
					y -= 1
					paths.append((x, y))
					continue
			if x - 1 >= 0:
				if map_[y][x - 1] != 1 and ((x - 1, y) not in paths):
					direction = LEFT
					continue
			if x + 1 < len(map_[y]):
				if map_[y][x + 1] != 1 and ((x + 1, y) not in paths):
					direction = RIGHT
					continue

			rev = paths.copy()
			rev.reverse()

			for i, p in enumerate(rev):
				rx, ry = p
				if rx - 1 >= 0:
					if map_[ry][rx - 1] != 1:
						res = checknexpre(rev, i, rx-1, ry)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = LEFT
							break

				if rx + 1 < len(map_[ry]):
					if map_[ry][rx + 1] != 1:
						res = checknexpre(rev, i, rx+1, ry)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = RIGHT
							break

				if ry - 1 >= 0:
					if map_[ry -1][rx] != 1:
						res = checknexpre(rev, i, rx, ry-1)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = UP
							break

				if ry + 1 < len(map_):
					if map_[ry + 1][rx] != 1:
						res = checknexpre(rev, i, rx, ry+1)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = DOWN
							break

				dead_end.add((rx, ry))

		if direction == LEFT:
			if x - 1 >= 0:
				if ((map_[y][x - 1] != 1) and ((x - 1, y) not in dead_end)):
					x -= 1
					paths.append((x, y))
					continue
			if y - 1 >= 0:
				if map_[y - 1][x] != 1 and ((x, y - 1) not in paths):
					direction = UP
					continue
			if y + 1 < len(map_):
				if map_[y + 1][x] != 1 and ((x, y + 1) not in paths):
					direction = DOWN
					continue

			rev = paths.copy()
			rev.reverse()

			for i, p in enumerate(rev):
				rx, ry = p
				if rx - 1 >= 0:
					if map_[ry][rx - 1] != 1:
						res = checknexpre(rev, i, rx-1, ry)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = LEFT
							break

				if rx + 1 < len(map_[ry]):
					if map_[ry][rx + 1] != 1:
						res = checknexpre(rev, i, rx+1, ry)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = RIGHT
							break

				if ry - 1 >= 0:
					if map_[ry -1][rx] != 1:
						res = checknexpre(rev, i, rx, ry-1)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = UP
							break

				if ry + 1 < len(map_):
					if map_[ry + 1][rx] != 1:
						res = checknexpre(rev, i, rx, ry+1)
						if res:
							paths = paths[:paths.index((rx, ry)) + 1]
							x, y = rx, ry
							direction = DOWN
							break

				dead_end.add((rx, ry))
except KeyboardInterrupt:
	pass
printpath(paths)#, dead_end)
print()
print(paths)