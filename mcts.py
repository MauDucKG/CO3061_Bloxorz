import time, sys
from ultis import *
from math import *
from random import randint, choice

class MCTSnode:
    def __init__(self, node: Node, f, monte: tuple = (0, 0)):
        self.node = node
        self.f = f
        self.h, self.length = monte
        

    def __lt__(self, mnode):
        return (self.h + self.f + self.length) < (mnode.h + mnode.f + mnode.length)
    
    def __eq__(self, anode) -> bool:
        return self.node == anode.node and self.f == anode.f and self.h == anode.h and self.length == anode.length
    
# monte carlo function
def playRandom(envir: State, mnode: MCTSnode, visited, maxstep = 5):
    curNode = mnode
    closelis = []
    step = 0

    for i in range(maxstep):
        #print("|   step ", step, ": ", curNode.node)
        closelis += [curNode.node]
        envir.set_player_position(curNode.node)
        if envir.check_goal():
            return (0, step)
        
        step += 1
        nextNodes = envir.next_position(curNode.node)
        validNode = []

        #temp = []
        for node in nextNodes:
            # if node not in open list, add node to list
            if node in closelis:
                continue
            
            flag = True
            for mnode in visited:
                if mnode.node == node:
                    if curNode.f + 1 >= mnode.f:
                        flag = False
                    break
            if flag: validNode.append(node)

            
        
        if validNode == []:
            return (100, maxstep)
        
        
        curNode = MCTSnode(choice(validNode), curNode.f + 1)

    return (envir.heuri(curNode.node), step)
            
        
def monteCarlo(envir: State, node: Node, f, visited, n = 5) -> MCTSnode:
    #print("monte node: ", node)
    #print("|   visited list:")
    #for mnode in visited:
        #print("    |   ", mnode.node)
    rnode = MCTSnode(node, f)
    sumHeuri = 0
    sumStep = 0
    #curNode = node
    for i in range(n):
        #print("- random ", i, ":")
        heuri, step = playRandom(envir, rnode, visited)
        sumHeuri += heuri
        sumStep += step
        #nextNode = 
    rnode.h = sumHeuri/n
    rnode.length = sumStep/n
    return rnode


def monteSearch(envir: State, n = 5):
    openlis = [MCTSnode(envir.start, sys.maxsize)]
    closelis = []
    nNode = 0

    while openlis != []:

        # find best candidate node
        nNode += 1 
        curNode = openlis[0]

        for node in openlis[1:]:
            if node < curNode:
                curNode = node
        

        # add current node to closelis, and remove from openlis
        #print(str(curNode.node))
        closelis.append(curNode)
        openlis.remove(curNode)
        # check node is goal
        envir.set_player_position(curNode.node)
        if envir.check_goal():
            break

        # add next node
        nextNodes = envir.next_position(curNode.node)
        #temp = []
        for node in nextNodes:
            # if node not in open list, add node to list
            flag = False
            for mnode in closelis:
                if mnode.node == node:
                    flag = True
                    break
            if not flag:
                for mnode in openlis:
                    if mnode.node == node:
                        flag = True
                        if curNode.f + 1 < mnode.f:
                            mnode.f = curNode.f + 1
                        break

                if not flag:
                    #temp.append(AStarNode(node, curNode.f + 1, envir.heuri(node)))
                    openlis.append(monteCarlo(envir, node, curNode.f + 1, openlis + closelis, n))
                    #bisect.insort_left(openlis, AStarNode(node, curNode.f + 1, envir.heuri(node)))
                    

        #print("add to open list: ")
        #for anode in temp:
            #print("|   ", anode.node)
        #print("open list: ")
        #for anode in openlis:
            #print("|   ", anode.node)
                

    # return path
    pointer = curNode.node
    path = []
    while pointer:
        path.insert(0, pointer)
        pointer = pointer.prev_node

    mem = 0
    if openlis != []: mem += len(openlis)*sys.getsizeof(openlis[0])
    if closelis != []: mem += len(closelis)*sys.getsizeof(closelis[0])

    return path, nNode, mem
