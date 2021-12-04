from helpers import read_grouped_lines 

import numpy as np

class BingoBoard(object):
    def __init__(self, lines):
        self.bd = np.zeros((5,5), dtype=np.int32)
        self.mp = {}
        for i, l in zip(range(5), lines):
            for j, x in zip(range(5), l.split()):
                x = int(x)
                self.bd[i, j] = x
                self.mp[x] = (i, j)
        self.rows_and_cols = np.zeros((2,5), dtype=np.int32)
        self.sum = np.sum(self.bd)
    
    def mark_number(self, num):
        if not num in self.mp:
            return None
        i, j = self.mp[num]
        self.sum -= num
        self.rows_and_cols[0, i] += 1
        self.rows_and_cols[1, j] += 1
        if self.rows_and_cols[0, i] == 5 or self.rows_and_cols[1, j] == 5:
            return self.sum * num


def solve_bingo(file, select_first):
    input = read_grouped_lines(file)
    orderd_numbers = [int(s) for s in input[0][0].split(",")]
    input = input[1:]
    boards = [BingoBoard(i) for i in input]
    for num in orderd_numbers:
        next_boards = []
        for board in boards:
            o = board.mark_number(num)
            if o:
                if select_first:
                    return o
                elif len(boards) == 1:
                    return o
            else:
                next_boards.append(board)
        boards = next_boards


def main():
    print(solve_bingo("in0", True))
    print(solve_bingo("in1", True))
    print(solve_bingo("in0", False))
    print(solve_bingo("in1", False))

if __name__ == "__main__":
    main()
