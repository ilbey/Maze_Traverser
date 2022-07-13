#2079242 - Ilbey Evcil
import time
startTime = time.time()

map_file = open("map.txt", "r")
map_str = map_file.read()

map_array = map_str.split("\n")
map_file.close()

def main():
    rows = len(map_array) - 1
    columns = len(map_array[0])
    vertices = []
    nodes = []
    i = 0
    j = 0
    while j < columns:
        i = 0
        while i < rows:
            if map_array[i][j] != '*' and map_array[i][j] != ' ':
                vertices.append([i,j])
                nodes.append(map_array[i][j])
            i = i + 1
        j = j + 1

    weight = []
    counter = 0
    for i in vertices:
        weight.append([])
        for j in vertices:
            x = helperFunc(i,j)
            weight[counter].append(x)
            
        counter = counter + 1        
    
    x = 0
    while x < len(vertices):
        y = x
        while y < len(vertices):
            if nodes[x] != nodes[y] or [nodes[x],nodes[y]] != [nodes[y],nodes[x]]:
                print("{},{},{}".format(nodes[x],nodes[y],weight[x][y]))
            y = y + 1
        x = x + 1

    choice = input("Enter an algorithm(BFS or UCS): ")
    
    if choice == "BFS" or choice == "bfs":
        totalCost = bfs(weight, vertices)
        stat(vertices, 1, totalCost)
    elif choice == "UCS" or choice == "ucs":
        totalCost = ucs(weight, vertices)
        stat(vertices, 2, totalCost)
    else:
        print("Entered wrong input!")


def stat(vertices, choice, totalCost):
    print("Statistics: ")
    print("\tNodes\tTime(ms)\tCost")
    if choice == 1:
        print("BFS\t{}\t{}\t\t{}".format(len(vertices), round((time.time() - startTime)*100,3), totalCost))
    elif choice == 2:
        print("UCS\t{}\t{}\t\t{}".format(len(vertices), round((time.time() - startTime)*100,3), totalCost))

def ucs(graph, vertices):
    path = []
    path.append(vertices[0])
    control = []
    tempElem = []
    total = 0
    num = len(vertices)
    i = 0
    j = 0
    counter = 0
    tempControl = []
    while counter < num - 1:
        if j < num:
            control.append(j)
            i = 0
            while i < num:
                if (i not in control):
                    if graph[i][j] != 0:
                        tempControl.append(i)
                        tempElem.append(graph[i][j])
                    else:
                        tempElem.append(100)
                i = i + 1
            i = 0
            temp = 100
            x = 0
            while x < len(tempElem):
                if tempElem[x] < temp:
                    temp = tempElem[x]
                    jTemp = tempControl[x]
                    j = jTemp
                x = x + 1
                if x >= len(tempElem):
                    tempElem = []
                    tempControl = []
                    total = total + temp
                    control.append(jTemp)
                    path.append(vertices[j])
        counter = counter + 1
    dx = abs(vertices[j][0] - vertices[0][0])
    dy = abs(vertices[j][1] - vertices[0][1])
    total = total + dx + dy
    path.append(vertices[0])
    
    print("Algorithm Used: UCS")
    countPrint = 0
    for x in coordToChar(path):
        if countPrint < len(vertices):
            print(x, end = "-")
        else: 
            print(x)
        countPrint = countPrint + 1
    print("Total Tour Cost: ",total)
    return total


def coordToChar(path):
    i = 0
    for elem in path:
        path[i] = map_array[elem[0]][elem[1]]
        i = i + 1
    return path


def bfs(graph, vertices):
    k = 0
    j = 0
    i = 1
    path = []
    totalCost = 0
    while j < len(vertices):
        totalCost = totalCost + graph[i][k]
        path.append(vertices[j])
        j = j + 1
        if i < len(vertices) - 1:
            i = i + 1
        else: 
            i = 0
    k = k + 1
    i = 0
    totalCost = totalCost + graph[i][k]
    path.append(vertices[0])
    countPrint = 0
    print("Algorithm Used: BFS")
    path = coordToChar(path)
    for x in path:
        if countPrint < len(vertices):
            print(x, end = "-")
        else: 
            print(x)
        countPrint = countPrint + 1
    print("Total Tour Cost: ",totalCost)
    return totalCost


def helperFunc(current,goal):
    htotal = 0
    counter = 0
    control = []
    
    while(current != goal):
        harray = AStar(current,goal)

        if harray[1] == 1:
            a = [current[0], current[1] + 1]
        elif harray[1] == 2:
            a = [current[0] - 1, current[1]]
        elif harray[1] == 3:
            a = [current[0] + 1, current[1]] 
        elif harray[1] == 4:
            a = [current[0], current[1] - 1]

        if a not in control:
            current = a
            control.append(a)
        else:
            a = [current[0], current[1] + 1]
            if a not in control and map_array[current[0]][current[1] + 1] != '*':
                current = a
                control.append(a)
            else:
                if map_array[current[0]+1][current[1]] != '*':
                    a = [current[0] + 1, current[1]] 
                    current = a
                    control.append(a)
                else:
                    a = [current[0], current[1] - 1] 
                    current = a
                    control.append(a)

        htotal = htotal + harray[0]
        counter = counter + 1
    return counter

  
def AStar(current,goal):
    f = 15
    gn = 1
    fup = 15
    fdown = 15
    fright = 15
    fleft = 15
    
  
    #right
    if map_array[current[0]][current[1]+1] != "*":
        hx = abs(current[0] - goal[0])
        hy = abs((current[1]+1) - goal[1])
        fright = hx + hy + gn

    if fright <= f:
        f = fright
        pos = 1

    #up
    if map_array[current[0]-1][current[1]] != "*":
        hx = abs((current[0]-1) - goal[0])
        hy = abs(current[1] - goal[1])
        fup = hx + hy + gn

    if fup <= f:
        f = fup
        pos = 2

    #down
    if map_array[current[0]+1][current[1]] != "*":
        hx = abs((current[0]+1) - goal[0])
        hy = abs(current[1] - goal[1])
        fdown = hx + hy + gn
    
    if fdown <= f:
        f = fdown
        pos = 3
    
    #left
    if map_array[current[0]][current[1]-1] != "*":
        hx = abs(current[0] - goal[0])
        hy = abs((current[1]-1) - goal[1])
        fleft = hx + hy + gn
    
    if fleft < f:
        f = fleft
        pos = 4

    f = f - 1
    return [f,pos]


if __name__ == "__main__":
    main()
