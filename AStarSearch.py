nodes = []     #For storing the names of the nodes
adj_list = {}  #For storing the adjacent nodes
dic={}         #For storing all the paths
sld={}         #For storing straight line distance
n=0            #For storing the number of nodes
def add_node(node):
    if node not in nodes:       #Checking whether the node already exists.
        nodes.append(node)   
        adj_list[node] = list() #Appending to the adjacency list for storing the adjacent nodes.
    else:
        print("Node is already present")

#fr => souce node
#to => destination node
#val => weights
def add_edge(fr,to,val):
    temp = [to,val]
    adj_list[fr].append(temp)
    temp2 = [fr,val]
    adj_list[to].append(temp2)

# grp => adjacent list
# dic => all paths
# key => optimal cost as for now
# list => optimal path as for now

def astar(grp,dic,key,lis,goal):
    global n
    flag=0
    visited=[0 for i in range(n)]          #For tracking the visited nodes.
    for i in range(0,len(lis)):
       visited[nodes.index(lis[i][0])]=1   #Setting all the nodes in the optimal path as visited
    s=lis[-1][0]                           #Getting the last node name for extending
    old_cost=lis[-1][1]                    #Getting the last node cost 
    if(s==goal):                           #If the current node is the goal then print result and return
       print("-------------------------------------------------------------------------------------")
       print("Optimal path:",dic[key])
       print("Optimal cost:",key)
       print("-------------------------------------------------------------------------------------")
       return
    adj_nodes=grp.get(s,[])                #Getting adjacent nodes for the current node
    for (node2,cost) in adj_nodes:
       cost=cost+old_cost
       if(visited[nodes.index(node2)]==1): #If the adjacent node is already visited,then leave that node
          continue
       sd=sld.get(node2)
       new_cost=cost+sd
       if(new_cost==key):                  #If the new cost is already present in all paths then set flag as 
          flag=1
       dic[new_cost]=lis.copy()            #Adding the new path to the dictionary
       new_path=(node2,cost)               
       dic[new_cost].append(new_path)      #Appending the expended node to the path.
       print(dic[new_cost],":",new_cost)
    if(flag==0):                           #If the new cost and the old cost equals then keep the path as well otherwise pop it
       dic.pop(key)
    my_keys=list()
    my_keys=list(dic.keys())
    my_keys.sort()                         #Sort the keys and get the optimal cost at first.
    print(my_keys)
    astar(grp,dic,my_keys[0],dic[my_keys[0]],goal)

def path_cost(path):
    total_cost = 0
    for(node,cost) in path:
            total_cost += cost
    return total_cost,path[-1][0]




def main():
    global n
    op = 0
    
    while(op <= 3):
        print("1.Adding Nodes      2.Adding edges     3.A-Star   4.Exit")
        op = int(input())
        if op == 1:
            print("Enter the number of nodes")
            n = int(input())
            print("Enter the nodes present in the graph")
            for i in range(0,n):
                    node = input()
                    add_node(node)
            print(nodes)
            print(adj_list)
        if op == 2:
            print("Enter the number of edges")
            e = int(input())
            print("Enter the edges in the graph")
            print("Enter the edges for each node like 'FROM' 'TO' 'EDGE VALUE'")
            for i in range(0,e):
                val = input().split(" ")
                add_edge(val[0],val[1],int(val[2]))
            print(adj_list)
        if op == 3:
            file = open('input.txt', 'r')
            for z in range(n):
                val=int(file.readline())     #Reading straight line distance from file.
                sld[nodes[z]]=val
            
            print("Enter the start node")
            st = input()
            print("Enter the end node")
            gl = input()
            v=sld[st]
            dic={v:[(st,0)]}
            astar(adj_list,dic,v,dic[v],gl)

main()