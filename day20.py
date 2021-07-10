import numpy as np
import re
from collections import Counter

from helpers import solve_grouped_task


def canonical_form(t):
    r = "".join(t)
    return min(r, r[::-1])


def parse_tile(lines):
    id = int(re.findall("\d+", lines[0])[0])
    tile = np.array([list(s) for s in lines[1:]])
    edges = [tile[0, :], tile[-1, :], tile[:, 0], tile[:, -1]]
    edges = ["".join(edge) for edge in edges]
    edges = [min(edge, edge[::-1]) for edge in edges]
    return id, edges, tile


def find_corners(tiles):
    edges_counter = Counter()
    for _, edges, _ in tiles:
        edges_counter.update(edges)
    res = []
    for id, edges, _ in tiles:
        #print([edges_counter[edge] for edge in edges])
        if [edges_counter[edge] for edge in edges].count(1) == 2:
            res.append(id)
    return res, edges_counter


def generate_tile_rotation(tile):
    def rotate(tile):
        res = tile.copy()
        nn = res.shape[0]
        for i in range(nn):
            for j in range(nn):
                res[nn-j-1, i] = tile[i,j]
        return res

    yield tile
    yield tile[::-1]
    for _ in range(3):
        tile = rotate(tile)
        yield tile
        yield tile[::-1]



def match_tile(left, upper, tiles, edges_counter, used):
    #assert(left or upper)
    for id, edges, tile in tiles:
        if id in used:
            continue
        if left and (left not in edges):
            continue
        if upper and (upper not in edges):
            continue
        for rtile in generate_tile_rotation(tile):
            cleft = canonical_form(rtile[:,0])
            cupper = canonical_form(rtile[0,:])
            left_match = (left and left == cleft) or (not left and edges_counter[cleft]==1)
            up_match = (upper and upper == cupper) or (not upper and edges_counter[cupper]==1)
            if left_match and up_match:
                used.add(id)
                return rtile

MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]
MSIZE = len(MONSTER), len(MONSTER[0])

def find_monsters_in_image(image):
    image = image.copy()
    n = image.shape[0]
    
    assert(n == image.shape[1])
    mc = 0
    for i in range(n):
        for j in range(n):
            if i + MSIZE[0] > n or j+MSIZE[1] > n:
                continue
            found = True
            for ii in range(MSIZE[0]):
                for jj in range(MSIZE[1]):
                    if MONSTER[ii][jj] == "#" and image[i+ii, j+jj] != "#":
                        found = False
            if found:
                mc += 1
                for ii in range(MSIZE[0]):
                    for jj in range(MSIZE[1]):
                        if MONSTER[ii][jj] == "#":
                            image[i+ii, j+jj] = 'O'
    return mc, np.sum(image == "#"), image


def find_monsters(tiles):
    corners, edges_counter = find_corners(tiles)
    n = int(np.sqrt(len(tiles)))
    
    rows = []
    last_uppers = [""] * n
    used = set()
    for _ in range(n):
        last_left = ""
        row = []
        for j in range(n):
            tile = match_tile(last_left, last_uppers[j], tiles, edges_counter, used)
            last_left = canonical_form(tile[:, -1])
            last_uppers[j] = canonical_form(tile[-1, :])
            row.append(tile[1:-1,1:-1])
        rows.append(np.hstack(row))
    final_image = np.vstack(rows)

    monsters_count = 0
    res = 0
    for image in generate_tile_rotation(final_image):
        mc, r, img = find_monsters_in_image(image)
        if mc > monsters_count:
            monsters_count = mc
            res = r
            print(mc, r)
            for zz in img:
                print("".join(zz))
    return res
        

def main_1():
    print(solve_grouped_task("in", parse_tile, lambda tiles: np.prod(find_corners(tiles)[0])))


def main():
    print(solve_grouped_task("in", parse_tile, find_monsters))


if __name__ == "__main__":
    main()
