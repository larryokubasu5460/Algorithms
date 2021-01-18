# create graph using adjacency matrix
INF=9999999
G=[[0,9,75,0,0],
[9,0,95,19,42],
[75,95,0,51,66],
[0,19,51,0,31],
[0,42,66,31,0]]
# number of vertices
v=5
selected=[0,0,0,0,0]
no_edge=0
# select zero vertex and make it true
selected[0]=True
print('Edge: Weight\n')
while (no_edge < v-1):
    minimum=INF
    x,y=0,0
    for i in range(v):
        if selected[i]:
            for j in range(v):
                if ((not selected[j]) and G[i][j]):
                    # not in selected and there is an edge
                    if minimum > G[i][j]:
                        minimum=G[i][j]
                        x,y=i,j
    print(str(x)+ "-" +str(y)+ ":" + str(G[x][y]))
    selected[y]=True
    no_edge += 1

