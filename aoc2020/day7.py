import re

from helpers import solve_line_task 

def parse_graph_edge_reversed(line):
    #dark coral bags contain 5 drab lime bags, 1 light brown bag, 3 pale blue bags.
    start_vertex, end_vertices = line.split(" contain ")
    start_vertex = " ".join(start_vertex.split()[:2])
    list_parsed = re.findall(r"\d+ ([\w ]+) bag[s]*", end_vertices)
    #list_parsed = re.findall(r"\d+[\w ]+", end_vertices)
    #list_parsed = [" ".join(s.split()[1:3]) for s in list_parsed]
    return [(out, start_vertex) for out in list_parsed]

def parse_graph_line(line):
    #dark coral bags contain 5 drab lime bags, 1 light brown bag, 3 pale blue bags.
    start_vertex, end_vertices = line.split(" contain ")
    start_vertex = " ".join(start_vertex.split()[:2])
    list_parsed = re.findall(r"(\d+) ([\w ]+) bag[s]*", end_vertices)
    list_parsed = [(bag, int(count)) for count, bag in list_parsed]
    # list_parsed = re.findall(r"\d+[\w ]+", end_vertices)
    # list_parsed = [(" ".join(s.split()[1:3]), int(s.split()[0])) for s in list_parsed]
    return (start_vertex, [out for out in list_parsed])

def compute_dfs(edges_lists):
    graph = {}
    for edges in edges_lists:
        for inv, outv in edges:
            l = graph.get(inv, [])
            l.append(outv)
            graph[inv] = l
    
    bfs = ["shiny gold"]
    visited = set(["shiny gold"])
    while bfs:
        v = bfs.pop()
        for neighbour in graph.get(v, []):
            if neighbour not in visited:
                visited.add(neighbour)
                bfs.append(neighbour)
    return len(visited)-1

def compute_counts(graph_lines):
    graph = dict(graph_lines)
    memoization = {}

    def compute_vertex(vertex):
        if vertex in memoization:
            return memoization[vertex]
        ans = sum([compute_vertex(neighbour)*count for neighbour, count in graph[vertex]]) + 1
        memoization[vertex] = ans
        return ans
    
    return compute_vertex("shiny gold")-1

def main_1():
  print(solve_line_task("in1", parse_graph_edge_reversed, compute_dfs))
  print(solve_line_task("in", parse_graph_edge_reversed, compute_dfs))

def main_2():
  print(solve_line_task("in1", parse_graph_line, compute_counts))
  print(solve_line_task("in2", parse_graph_line, compute_counts))
  print(solve_line_task("in", parse_graph_line, compute_counts))

if __name__ == "__main__":
    main_2()