from pprint import pprint
from termcolor import cprint

map_ = """\
111011101111100
001010000010000
001011000010000
000000000000111
111011000000100
001001000000111
001001000000100
000001001000111
001010001110000
001010001000011
111011101000001
000000000000011
001111100010000
001000000010100
101010001011100
001000000010000
001000010011100
001000010000100"""


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

    def fill_up(self):
        for y, col in enumerate(self.map):
            for x, pos in enumerate(col):
                if pos == 1 and (x, y) not in self.filled:
                    self.filled.add((x, y))

                    self.thought_box(x, y, col)

    def thought_box(self, x, y, col):
        self.map[y][x] = 3
        fill_start_x = x
        for i in range(x + 1, len(col)):
            if self.map[y][i] == 1:
                self.filled.add((i, y))
            if y + 1 < len(self.map):
                if self.map[y + 1][i] == 1:
                    for e in range(y + 1, len(self.map)):
                        if self.map[e][i] == 1:
                            self.filled.add((i, e))
                            for tx in range(fill_start_x, i):
                                self.map[e][tx] = 2
                                self.filled.add((tx, e))
                        else:
                            break
                    fill_start_x = i + 1
                elif self.map[y][i] == 0:
                    if fill_start_x != x:
                        for e in range(y + 1, len(self.map)):
                            if self.map[e][fill_start_x - 1] == 1:
                                for tx in range(fill_start_x, i):
                                    self.map[e][tx] = 2
                                    self.filled.add((tx, e))
                            else:
                                break
                    break
        
        fill_start_y_l = y
        fill_start_y_r = y
        for e in range(y + 1, len(self.map)):
            if self.map[e][x] == 1:
                self.filled.add((x, e))
            if x + 1 < len(col):
                if self.map[e][x + 1] == 1:
                    for i in range(x + 1, len(col)):
                        if self.map[e][i] == 1:
                            self.filled.add((i, e))
                            for ty in range(fill_start_y_r, e):
                                self.map[ty][i] = 2
                                self.filled.add((i, ty))
                        else:
                            break
                    fill_start_y_r = e + 1
                elif self.map[e][x] == 0:
                    if fill_start_y_r != y:
                        for i in range(x + 1, len(col)):
                            if self.map[fill_start_y_r - 1][i] == 1:
                                for ty in range(fill_start_y_r, e):
                                    self.map[ty][i] = 2
                                    self.filled.add((i, ty))
                            else:
                                break
                    else:
                        break
            if x - 1 >= 0:
                if self.map[e][x - 1] == 1 and (x - 1, e) not in self.filled:
                    for i in range(x - 1, -1, -1):
                        if self.map[e][i] == 1:
                            self.filled.add((i, e))
                            for ty in range(fill_start_y_l, e):
                                self.map[ty][i] = 2
                                self.filled.add((i, ty))
                        else:
                            break
                    fill_start_y_l = e + 1
                elif self.map[e][x] == 0:
                    if fill_start_y_l != y:
                        for i in range(x - 1, -1, -1):
                            if self.map[fill_start_y_l - 1][i] == 1:
                                for ty in range(fill_start_y_l, e):
                                    self.map[ty][i] = 2
                                    print(x, y)
                                    self.filled.add((i, ty))
                            else:
                                break
                    break
        if fill_start_y_r != y and self.map[e][x] == 1:
            for i in range(x + 1, len(col)):
                if self.map[fill_start_y_r - 1][i] == 1:
                    for ty in range(fill_start_y_r, len(self.map)):
                        self.map[ty][i] = 2
                        self.filled.add((i, ty))
                else:
                    break
        if fill_start_y_l != y and self.map[e][x] == 1:
            for i in range(x - 1, -1, -1):
                if self.map[fill_start_y_l - 1][i] == 1:
                    for ty in range(fill_start_y_l, len(self.map)):
                        self.map[ty][i] = 2
                        self.filled.add((i, ty))
                else:
                    break

        if y + 1 < len(self.map):
            if self.map[y + 1][x] == 1:
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

    def format(self):
        newmap = []
        for col in self.map:
            newmap.append([])
            for pos in col:
                if pos == 0:
                    newmap[-1].append(0)
                else:
                    newmap[-1].append(1)
        self.map = newmap

    def print(self):
        map_ = self.map
        cprint(" " * (len(map_[0]) * 2 + 4), "yellow", "on_yellow")
        for col in map_:
            cprint("  ", "yellow", "on_yellow", end="")
            for row in col:
                if row == 0:
                    cprint("  ", "white", "on_white", end="")
                elif row == 1:
                    cprint("  ", "grey", "on_grey", end="")
                elif row == 2:
                    cprint("  ", "blue", "on_blue", end="")
                elif row == 3:
                    cprint("  ", "red", "on_red", end="")
            cprint("  ", "yellow", "on_yellow")
        cprint(" " * (len(map_[0]) * 2 + 4), "yellow", "on_yellow")


if __name__ == "__main__":
    map_ = parse_map(map_)
    m = Map(map_)
    m.fill_up()
    m.format()
    m.print()
