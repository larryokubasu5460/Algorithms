# creating a graph using adjacency lists
# use a dictionary to represet it


# print(graph)
# using the iterative method

def dfs_iterative(graph,source):
    if source is None or source not in graph:
        return "invalid input"
    path=[]
    stack=[source]
    while len(stack)!= 0:
        s=stack.pop()
        if s not in path:
            path.append(s)
        if s not in graph:
            # leaf node
            continue
        for neighbor in graph[s]:
            stack.append(neighbor)
    return " ".join(path)




def dfs_recursive(graph,source,path=[]):
    if source not in path:
        path.append(source)
        if source not in graph:
            # leaf node, back track
            return path
        for neighbor in graph[source]:
            path=dfs_recursive(graph,neighbor,path)
    return path
graph = {"A":["D","C","B"],
   "B":["E"],
   "C":["G","F"],
   "D":["H"],
   "E":["I"],
   "F":["J"]}
graphe={"A":["B","C","D"],
"B":["E"],
"C":["F","G"],
"D":["H"],
"E":["I"],
"F":["J"]}
print(dfs_iterative(graph,"A"))
path=dfs_recursive(graphe,"A")
print(" ".join(path))