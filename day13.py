from helpers import solve_line_task 
import re

def folding_task(lines, num_folds=-1):
    dots = []
    blank = lines.index("")
    for l in lines[:blank]:
        dots.append([int(x) for x in l.split(",")])
    
    for fold in lines[blank+1:]:
        param, inx = re.findall("(\w)=(\d+)", fold)[0]
        inx = int(inx)
        for d in dots:
            if param[0] == 'x':
                flip = 0
            else:
                flip = 1
            if d[flip] > inx:
                d[flip] = 2*inx - d[flip]
            if d[flip] == inx:
                print("error", d[flip], inx, flip)

        tuple_dots = set([tuple(d) for d in dots])
        dots = [list(d) for d in tuple_dots]
        num_folds -= 1
        if num_folds == 0:
            break
    maxx = max([d[0] for d in dots])+1
    maxy = max([d[1] for d in dots])+1
    paper = [" "*maxx for l in range(maxy)]
    for d in dots:
        paper[d[1]] = paper[d[1]][:d[0]] + '#' + paper[d[1]][d[0]+1:]
    for p in paper:
        print(p)
    return len(dots)


def main():
    print(solve_line_task("cin0", str, folding_task))
    print(solve_line_task("cin1", str, folding_task))


if __name__ == "__main__":
    main()
