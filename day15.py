import re

def word_spoken(initial, round):
    initial = [int(s) for s in initial.split(",")]
    last_occurrence = dict()
    last = -1
    for i in range(0,round):
        if i < len(initial):
            say = initial[i]
        elif last not in last_occurrence:
            say = 0
        else:
            say = i-last_occurrence[last]
        last_occurrence[last] = i
        last = say
    return last

def main():
    # for i in range(4,12):
    print(word_spoken("0,3,6", 30000000))
    print(word_spoken("5,2,8,16,18,0,1", 30000000))


if __name__ == "__main__":
    main()
