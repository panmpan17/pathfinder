from termcolor import cprint
from mapfillup import *

UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"

class Deadend(list):
    def add(self, par):
        self.append(par)

class BMap(Map):
    def __init__(self, map_=[]):
        # super(Map).__init__()
        self.filled = set()
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

    def find_path(self, pos, end):
        # self.fill_up()
        self.format()

        self.map[end[1]][end[0]] = 2

        self.x, self.y = pos
        self.paths = [(self.x, self.y)]

        self.dead_end = Deadend()
        self.paths_tested = set(self.paths)
        self.direction = DOWN

        while self.map[self.y][self.x] != 2:
            if self.direction == DOWN:
                if self.y + 1 < len(self.map):
                    if ((self.map[self.y + 1][self.x] != 1) and
                            ((self.x, self.y + 1) not in self.dead_end) and
                            ((self.x, self.y + 1) not in self.paths)):
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
                            ((self.x + 1, self.y) not in self.dead_end) and
                            ((self.x + 1, self.y) not in self.paths)):
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
                            ((self.x, self.y - 1) not in self.dead_end) and
                            ((self.x, self.y - 1) not in self.paths)):
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
                            ((self.x - 1, self.y) not in self.dead_end) and
                            ((self.x - 1, self.y) not in self.paths)):
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

        cprint(" " * (len(self.map[0]) * 2 + 4), "yellow", "on_yellow")
        for y, row in enumerate(self.map):
            cprint("  ", "yellow", "on_yellow", end="")
            for x, line in enumerate(row):
                if line == 0:
                    print("  ", end="")
                elif line == 1:
                    cprint("  ", "white", "on_white", end="")
                elif line == 2:
                    print(" H", end="")
                elif line == 3:
                    seq = self.paths.index((x, y))
                    cprint(f"{seq}", "red", "on_red", end="")
                    if seq < 10:
                        cprint(" ", "red", "on_red", end="")
                elif line == 4:
                    seq = self.dead_end.index((x, y))
                    cprint(f"{seq}", "grey", "on_blue", end="")
                    if seq < 10:
                        cprint(" ", "grey", "on_blue", end="")
            cprint("  ", "yellow", "on_yellow")
        cprint(" " * (len(self.map[0]) * 2 + 4), "yellow", "on_yellow")


if __name__ == "__main__":
    map_ = parse_map(map_)
    m = BMap(map_=map_)
    try:
        m.find_path((3, 0), (len(map_[0]) - 1, len(map_) - 1))
    except KeyboardInterrupt:
        pass
    m.printpath()
