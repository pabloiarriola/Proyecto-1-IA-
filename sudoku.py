from collections import OrderedDict
#from random import randint
import sys
#variables globales
Entrada = ""
Entrada = sys.argv[1]
L = list(Entrada)
sudoku = [0 if x=="." else int(x)for x in Entrada]
proto_sudoku = sudoku[:]
frontier = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
values_present = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
cleaner = []
current_node = 0
possible_values = [1,2,3,4]
nodes = {}
actions = {}
ordered_actions = {}
action_keys = []
visitados = {}
full_counter = 0
#for i in range(4):
    #filas
   # nodes[0].append(sudoku[i])
    #columnas
  #  if(i !=0):
 #       nodes[0].append(sudoku[i*4])
    #cuadro adyacente    
#nodes[0].append(sudoku[5])


#rows
row1 = []
row2 = []
row3 = []
row4 = []
def fill_rows():
    global row1,row2,row3,row4,sudoku
    row1 = sudoku[0:4]
    row2 = sudoku[4:8]
    row3 = sudoku[8:12]
    row4 = sudoku[12:16]
    
#cols
col1 = []
col2 = []
col3 = []
col4 = []

def fill_cols():
    global col1,col2,col3,col4,sudoku
    
    col1 = (sudoku[0:1]+ sudoku[4:5] + sudoku[8:9]+ sudoku[12:13])
    col2 = (sudoku[1:2]+ sudoku[5:6] + sudoku[9:10]+ sudoku[13:14])
    col3 = (sudoku[2:3]+ sudoku[6:7] + sudoku[10:11]+ sudoku[14:15])
    col4 = (sudoku[3:4]+ sudoku[7:8] + sudoku[11:12]+ sudoku[15:16])
        

#nodos

node1 =  []
node2 =  []
node3 =  []
node4 =  []
node5 =  []
node6 =  []
node7 =  []
node8 =  []
node9 =  []
node10 = []
node11 = []
node12 = []
node13 = []
node14 = []
node15 = []
node16 = []

def create_update_nodes():
    global node1,node2,node3,node4,node5,node6,node7,node8,node9,node10,node11,node12,node13,node14,node15,node16,nodes
    
    node1.append(row1 + col1[1:] + col2[1:2])
    node2.append(row1 + col2[1:] + col1[1:2])
    node3.append(row1 + col3[1:] + col4[1:2])
    node4.append(row1 + col4[1:] + col3[1:2])
    #el skip no se ve muy bien pero se ordena de la manera mas facil de asegurarse que estan todos los numeros
    node5.append(row2 + col1[0:1] + col1[2:] + row1[1:2])
    node6.append(row2 + col2[0:1] + col2[2:] + row1[0:1])
    node7.append(row2 + col3[0:1] + col3[2:] + col4[0:1])
    node8.append(row2 + col4[0:1] + col4[2:] + col3[0:1])
    #3er fila
    node9.append( row3 + col1[0:2] + col1[3:] + row4[1:2])
    node10.append(row3 + col2[0:2] + col2[3:] + row4[0:1])
    node11.append(row3 + col3[0:2] + col3[3:] + row4[3:4])
    node12.append(row3 + col4[0:2] + col4[3:] + row4[2:3])
    #4a fila
    #ya no hay skip como la primera fila
    node13.append(row4 + col1[:3] + row3[1:2])
    node14.append(row4 + col2[:3] + row3[0:1])
    node15.append(row4 + col3[:3] + row3[3:4])
    node16.append(row4 + col4[:3] + row3[2:3])

    nodes[0]  = node1
    nodes[1]  = node2
    nodes[2]  = node3
    nodes[3]  = node4
    nodes[4]  = node5
    nodes[5]  = node6
    nodes[6]  = node7
    nodes[7]  = node8
    nodes[8]  = node9
    nodes[9]  = node10
    nodes[10] = node11
    nodes[11] = node12
    nodes[12] = node13
    nodes[13] = node14
    nodes[14] = node15
    nodes[15] = node16


#frontera
def fill_frontier():
    global frontier, nodes, values_present
    for i in range(16):    
        for value in nodes[i]:
            if value not in values_present[i] and value != 0:
                values_present[i].append(value)
                frontier[i].append(list(set(possible_values)-set(values_present[i][0])))

#print(frontier)
def fill_actions():
    global sudoku,actions,frontier
    for i in range(16):
        if(sudoku[i]==0):
            actions[i] = frontier[i][0]


        
#print(len(actions[2]))
#print(len([1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]))

#ordenar de menor a mayor las acciones
def actionkeys():
    global action_keys,ordered_actions
    ordered_actions = OrderedDict(sorted(actions.items(), key = lambda item: len(item[1]),reverse = False))
    action_keys = list(ordered_actions.keys())


#print(action_keys)
#print(ordered_actions)
#eliminar opciones con 1 posibilidad
#resolver sudoku
def solve():
    global action_keys,ordered_actions,sudoku
    for i in range(len(action_keys)):
        if(len(ordered_actions[action_keys[i]]) ==1):
            sudoku[action_keys[i]] = ordered_actions[action_keys[i]].pop()
        #elif(len(ordered_actions[action_keys[i]])>1):
         #   sudoku[action_keys[i]] = ordered_actions[action_keys[i]][randint(0,len(ordered_actions[action_keys[i]])-1)]


while(0 in sudoku and full_counter<16):
    #llenar filas columnas y nodos
    fill_rows()
    fill_cols()
    create_update_nodes()
    #frontier
    fill_frontier()
    #actions
    fill_actions()
    #keys
    actionkeys()
    solve()
    print(sudoku)
    #terminan las acciones de llenado
    #vaciar
    #vaciar diccionario nodos
    nodes.clear()
    #vaciar nodos
    node1.clear()
    node2.clear()
    node3.clear()
    node4.clear()
    node5.clear()
    node6.clear()
    node7.clear()
    node8.clear()
    node9.clear()
    node10.clear()
    node11.clear()
    node12.clear()
    node13.clear()
    node14.clear()
    node15.clear()
    node16.clear()

    #vaciar frontera y acciones y values_present
    values_present.clear()
    frontier.clear()
    actions.clear()
    for i in range(16):
        frontier.append([])
        values_present.append([])

    #vaciar action_keys y ordered actions
    action_keys.clear()
    ordered_actions.clear()
    full_counter += 1

#fin del while
if(0 in sudoku):
    print("no es posible resolver este sudoku")

#llenar filas columnas y nodos
#fill_rows()
#fill_cols()
#create_update_nodes()

#frontier
#fill_frontier()
#print(frontier)
#actions
#fill_actions()
#keys
#actionkeys()
#print(action_keys)
#print(ordered_actions)
#solve()
#print(sudoku)

