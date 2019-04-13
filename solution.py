def sublevel_persistence(graph):
    n_points = len(graph)

    ### Build minima and maxima ############################################
    maxima = []
    minima = []
    graph.append([n_points, float('inf')])
    graph.append([-1, float('inf')])
    for i in range(0, n_points):
        if graph[i-1][1] < graph[i][1] and graph[i][1] > graph[i+1][1]:
            maxima.append(i)
        elif graph[i-1][1] > graph[i][1] and graph[i][1] < graph[i+1][1]:
            minima.append(i)

    maxima.append(n_points-1)
    maxima.insert(0, 0)
    ### Done building maxima and minima ###################################

    marked = set()
    z = 0
    out = []
    while z < len(minima):
        a = minima.index(sorted(minima, key = lambda x: graph[x][1])[z])
        val = graph[minima[a]][1]
        z += 1
        b = a+1
        best = -float('inf')
        kill = float('inf')
        for i in range(b, len(maxima)):
            if graph[maxima[i]][1] >= best:
                best = graph[maxima[i]][1]
                if maxima[i] in marked:
                    kill = best
                    break
                marked.add(maxima[i]) 
        best = -float('inf')
        for i in range(b-1, -1, -1):
            if graph[maxima[i]][1] >= best:
                best = graph[maxima[i]][1]
                if maxima[i] in marked:
                    kill = min(kill, best)
                    break
                marked.add(maxima[i]) 
        out.append( [val,kill] )
    return sorted(out, key = lambda x: abs(x[0] - x[1])) 
