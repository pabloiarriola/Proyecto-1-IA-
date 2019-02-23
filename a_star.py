class Node():
    def __init__(self,parent=None,position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self,other):
        return self.position == other.position

def astar(maze,start,end):
    #nodo inicial y final
    start_node = Node(None,start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None,end)
    end_node.g = end_node.h = end_node.f = 0
    #lista abierta y cerrada
    open_list = []
    closed_list = []
    #agregar nodo inicial
    open_list.append(start_node)
    #Loop hasta encontrar goal state o error
    while(len(open_list) > 0):
        #sobre el nodo actual
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if(item.f < current_node.f):
                current_node = item
                current_index = index
        #mover de lista abierta a cerrada
        open_list.pop(current_index)
        closed_list.append(current_node)

        #meta
        if(current_node == end_node):
            path = []
            current = current_node
            while(current is not None):
                path.append(current.position)
                current = current.parent
            #camino al revez
            return path[::-1]
        #hijos
        children = []
        for new_position in [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]:
            #posicion del nodo
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            #asegurarse que no se pase
            if node_position[0] >(len(maze)-1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1])-1) or node_position[1]<0:
                continue
            if maze[node_position[0]][node_position[1]] != 0:
                continue
            #nuevo nodo
            new_node = Node(current_node,node_position)
            #agregar nuevo nodo a hijos
            children.append(new_node)
        #loop en los hijos
        for child in children:
            #hijos en la lista cerrada
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            #f,g,h
            child.g = current_node.g + 1
            #child.h = ((child.position[0] - end_node.position[0])**2) + ((child.position[1] - end_node.position[1])**2)
            for i in range(4):
                for j in range(4):
                    value = estado_inicial[i][j]
                    if(value!= 0):
                        targetX = (value - 1) / 4
                        targetY = (value - 1) % 4
                        dx = i - targetX
                        dy = j - targetY
                        child.h += abs(dx) + abs(dy)
            child.f = child.g + child.h
            #hijo ya en lista abierta
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            #agregar hijo a lista abierta
            open_list.append(child)

def main():
    entrada = "F21C856B49A73ED."
    L = list(entrada)
    #print(L)
    estado_inicial_array = [0 if x=="." else int(x,16) for x in entrada]
    estado_inicial = [(estado_inicial_array[0:4]),(estado_inicial_array[4:8]),(estado_inicial_array[8:12]),(estado_inicial_array[12:16])]
    goal_state = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

##    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
##            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0,0)
    end = (7,6)
    path = astar(estado_inicial,estado_inicial,goal_state)
    print(path)
main()
        
