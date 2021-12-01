import numpy as np
import re

from contextlib import suppress

from helpers import read_grouped_lines, deduce

def ticket_scanning_error_rate(filename):
    rules, _, tickets = read_grouped_lines(filename)
    
    parsed_rules = []
    for r in rules:
        bounds = re.fullmatch("[\w ]+: (\d+)-(\d+) or (\d+)-(\d+)", r).groups()
        bounds = [int(b) for b in bounds]
        parsed_rules.append((bounds[0], bounds[1]))
        parsed_rules.append((bounds[2], bounds[3]))

    error_rate = 0
    for t in tickets[1:]:
        vals = [int(a) for a in t.split(",")]
        for v in vals:
            matched = False
            for lower_bound, upper_bound in parsed_rules:
                if lower_bound <= v <= upper_bound:
                    matched = True
                    break
            if not matched:
                error_rate += v
    return error_rate


def departure_values(filename):
    rules, your_ticket, tickets = read_grouped_lines(filename)
    
    parsed_rules = {}
    for r in rules:
        bounds = re.fullmatch("([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)", r).groups()
        name = bounds[0]
        bounds = [int(b) for b in bounds[1:]]
        parsed_rules[name] = bounds

    valid_tickets = []
    for t in tickets[1:]:
        vals = [int(a) for a in t.split(",")]
        is_valid = True
        for v in vals:
            matched = False
            for bounds in parsed_rules.values():
                if (bounds[0] <= v <= bounds[1]) or (bounds[2] <= v <= bounds[3]):
                    matched = True
                    break
            if not matched:
                is_valid = False
                break
        if is_valid:
            valid_tickets.append(vals)
    
    valid_tickets = np.array(valid_tickets)
    valid_values = valid_tickets.transpose()
    
    potential_fields = {}
    for name, bounds in parsed_rules.items():
        candidates = []
        for inx, values in enumerate(valid_values):
            if not [1 for v in values if not ((bounds[0] <= v <= bounds[1]) or (bounds[2] <= v <= bounds[3]))]:
                candidates.append(inx)
        potential_fields[name] = candidates
    
    deduced_fields = deduce(potential_fields)

    print(deduced_fields)

    your_ticket = [int(a) for a in your_ticket[1].split(",")]
    print(your_ticket)
    return np.prod([your_ticket[inx] for name, inx in deduced_fields.items() if name.startswith("departure")])

def main():
    # for i in range(4,12):
    #print(departure_values("in1"))
    print(departure_values("in"))


if __name__ == "__main__":
    main()
