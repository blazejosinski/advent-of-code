import copy
import re

#from helpers import solve_line_task

def solve_part1(filename):
    with open(filename, "r") as f:
        toa = int(f.readline())
        buses = [int(s) for s in f.readline().split(",") if s != "x"]
    sol = 10**9
    busb = -1
    for b in buses:
        if sol > (b-(toa%b)):
            sol = b-(toa%b)
            busb = b
    print(sol * busb)

def gcd(a,b):
    if a<b:
        return gcd(b,a)
    if b==0:
        return a
    return gcd(b, a%b)

def solve_part2(filename):
    with open(filename, "r") as f:
        _ = int(f.readline())
        buses = f.readline().split(",")
    lcm = int(buses[0])
    res = 0
    for t, n in enumerate(buses):
        if t == 0 or n == "x":
            continue
        n = int(n)
        t %= n
        while res % n != n-t:
            res += lcm
        lcm = lcm * n // gcd(lcm, n)        
    print(res)

def main():
    solve_part2("in")

if __name__ == "__main__":
    main()
