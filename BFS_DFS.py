from queue import Queue
from queue import LifoQueue
import sys
def add_node():
    #Extending the column by 1 for each row.
    for i in range (len(list)):
        list[i].append(0)
    
    #Appending a new row
    list.extend([[0]*(len(list)+1)])
    
def add_edge(i,j):
    #Updating the value from 0 to 1 in adjacent matrix 
    list[nodes.index(i)][nodes.index(j)]=1
    list[nodes.index(j)][nodes.index(i)]=1

def delete_node(v):
    # Delete the node name
    del list[nodes.index(v)]

    #Delete the last column in each row.
    for i in range(0,len(list)):
        del list[i][nodes.index(v)]

    #Delete the last row
    del nodes[nodes.index(v)]

def delete_edge(i,j):
    #Updating the values from 1 to 0
    list[nodes.index(i)][nodes.index(j)]=0
    list[nodes.index(j)][nodes.index(i)]=0

def adjacent_matrix():
    for i in range(len(list)):
        for j in range(len(list[i])):
                print(list[i][j]," ",end="")
        print("\n")

def display():
    for i in range(len(list)):
        print(str(nodes[i]),end="")
        for j in range(len(list[i])):
            if(list[i][j] == 1):
                print(" -> ",nodes[j],end="")
        print("\n")

def bfs(start_node ,goal_node):    
    visited=[0]*n      # To track whether the node is visited or not
    q = Queue()            
    q.put(start_node)          #Inserting the first value
    visited[nodes.index(start_node)]=1     #Setting the node as visited
    while(not q.empty()):
        a = q.get()
        print(a,"  ",end="")        
        if(a==goal_node):        #If the given node is the goal then break the loop
            break
        for i in range(0,n):            
            if(list[nodes.index(a)][i] == 1 and visited[i] ==0):      #Check whether the node is adjacent as well as not visited
                visited[i]=1
                q.put(nodes[i])
    print()

def dfs(start_node,goal_node):
    visited=[0]*n          # To track whether the node is visited or not
    stack = LifoQueue()
    stack.put(start_node)           #Inserting the first value
    visited[nodes.index(start_node)]=1     #Setting the node as visited
    while(not stack.empty()):
        a = stack.get()
        print(str(a)+"  ",end="")
        if(a == goal_node):        #If the given node is the goal then break the loop
            break
        for i in range(n-1,-1,-1):  #Reversely push the nodes
            if(list[nodes.index(a)][i] == 1 and visited[i] ==0):      #Check whether the node is adjacent as well as not visited
                visited[i]=1
                stack.put(nodes[i])
    print()


n = int(input("Enter the number of nodes of a graph :"))
list = [[0 for x in range(n)] for y in range(n)]
nodes = []

for i in range(n):
    name = input("Enter the name of the node :")
    while(name in nodes):     #Repeat loop until the node name is unique
        name = input("Name already exists..Enter another name :")
    nodes.append(name)

for i in range(0,n):
    m = int(input("Enter the number of adjacent nodes for node "+str(nodes[i])+" :"))
    for j in range(0,m):
        a = input("Enter the adjacent node :"+str((j+1))+" :")
        while(a not in nodes):     #Repeat loop until the node name exists
            a = input("No such nodes..Enter correct node :")
        list[i][nodes.index(a)]=1
        list[nodes.index(a)][i]=1

display()
print("Adjacent Matrix ")
adjacent_matrix()

ch =1
while(ch):
    x = int(input("MENU\n1.Add Node\n2.Add Edge\n3.Delete Node\n4.Delete Edge\n5.Adjacency Matrix\n6.Adjacency list\n7.BFS\n8.DFS\n9.Exit\nEnter your option :"))
    if(x==1):
        print("Enter the new node :",end ="")
        name = get_input(0)
        nodes.append(name)
        add_node()
        print("Node added successfully")
        display() 

    elif(x==2):
        print("Enter the source node :",end="")
        i = get_input(1)
        print("Enter the destination node :",end ="")
        j=get_input(1)
        add_edge(i,j)
        print("Edge added successfully")
        display()

    elif(x == 3):
        print("Enter the node to be deleted :",end ="")
        v = get_input(1)
        delete_node(v)
        print("Node deleted successfully")
        display()

    elif(x==4):
        print("Enter the source node :",end="")
        i = get_input(1)
        print("Enter the destination node :",end ="")
        j=get_input(1)
        delete_edge(i,j) 
        print("Edge deleted successfully")
        display()

    elif(x==5):
        print("Adjacncy Matrix")
        adjacent_matrix()

    elif(x==6):
        print("Display")
        display()
    
    elif(x==7):
        start_node = input("Enter the source node :")
        goal_node = input("Enter the destination node :")
        bfs(start_node,goal_node)

    elif(x==8):
        start_node = input("Enter the source node :")
        goal_node = input("Enter the destination node :")
        dfs(start_node,goal_node)

    elif(x==9):
        exit()
    else:
        print("Enter the valid option.")



