import re
import numpy as np

from helpers import solve_line_task 

def perform(v1, v2, op):
    if op == "+":
        return v1+v2
    return v1*v2

def parse_parenthesis(tokens, inx):
    assert(tokens[inx] == "(")
    value = 0
    last_op = "+"
    while True:
        inx += 1
        if tokens[inx] in ["*", "+"]:
            last_op = tokens[inx]
        elif tokens[inx].isdigit():
            value = perform(value, int(tokens[inx]), last_op)
        elif tokens[inx] == "(":
            paranthesis_value, inx = parse_parenthesis(tokens, inx)
            value = perform(value, paranthesis_value, last_op)
        else:
            return value, inx
        

def parse_line(line):
    tokens = ("("+line+")").replace("(", " ( ").replace(")", " ) ").split()
    return parse_parenthesis(tokens, 0)[0]


def parse_parenthesis2(tokens, inx):
    assert(tokens[inx] == "(")
    simple_tokens = []
    while True:
        inx += 1
        if tokens[inx] in ["*", "+"]:
            simple_tokens.append(tokens[inx])
        elif tokens[inx].isdigit():
            simple_tokens.append(tokens[inx])
        elif tokens[inx] == "(":
            paranthesis_value, inx = parse_parenthesis2(tokens, inx)
            simple_tokens.append(str(paranthesis_value))
        else:
            break
    text = "".join(simple_tokens)
    factors = text.split("*")
    factors = [sum([int(l) for l in f.split("+")]) for f in factors]
    return np.prod(factors), inx
        

def parse_line2(line):
    tokens = ("("+line+")").replace("(", " ( ").replace(")", " ) ").split()
    return parse_parenthesis2(tokens, 0)[0]


def main():
    print(solve_line_task("in", parse_line2, sum))

if __name__ == "__main__":
    main()
