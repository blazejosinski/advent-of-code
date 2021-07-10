import re

from helpers import solve_line_task 

MASK = "mask = "

def parse_line(line):
    if line.startswith(MASK):
        mask = line[len(MASK):]
        and_mask = "".join(["0" if b == "0" else "1" for b in mask])
        or_mask = "".join(["1" if b == "1" else "0" for b in mask])
        mask_len = len(mask)
        x_bin_locations = [mask_len-i-1 for i in range(mask_len) if mask[i]=='X']
        return (MASK, int(and_mask, base=2), int(or_mask, base=2), x_bin_locations)
    return re.findall(r"mem\[(\d+)\] = (\d+)", line)[0]


def process(lines):
    and_mask = None
    or_mask = None
    mem = {}
    for l in lines:
        if l[0] == MASK:
            and_mask, or_mask = l[1], l[2]
        else:
            address, value = int(l[0]), int(l[1])
            mem[address] = (value & and_mask) | or_mask
    return sum(mem.values())
            

def process_v2(lines):
    and_mask = None
    or_mask = None
    x_bin_locations = None
    mem = {}
    for l in lines:
        if l[0] == MASK:
            and_mask, or_mask, x_bin_locations = l[1], l[2], l[3]
        else:
            address, value = int(l[0]), int(l[1])
            address = address | or_mask
            for loc in x_bin_locations:
                if address & (1<<loc):
                    address ^= (1<<loc)
            for mask in range(2**len(x_bin_locations)):
                lmask = 0
                for i, loc in enumerate(x_bin_locations):
                    if mask & (1<<i):
                        lmask = lmask | (1<<loc)
                mem[address | lmask] = value
                #print(lmask, address | lmask)
    return sum(mem.values())


def main():
    print(solve_line_task("in1", parse_line, process_v2))
    print(solve_line_task("in", parse_line, process_v2))

if __name__ == "__main__":
    main()
