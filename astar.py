from ultis import *
import sys

class AStarNode:
    def __init__(self, node: Node, f, h):
        self.node = node
        self.f = f
        self.h = h

    def __lt__(self, node):
        return (self.f + self.h) < (node.f + node.h)
    
    def __eq__(self, anode) -> bool:
        return self.node == anode.node and self.f == anode.f and self.h == anode.h

def AStarSearch(envir: State, a = 1, b = 1, c = 1):
    openlis = [AStarNode(envir.start, 0, sys.maxsize)]
    closelis = []
    minNode = None

    while openlis != []:

        # find best candidate node
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
            for anode in closelis:
                if anode.node == node:
                    flag = True
                    break
            if not flag:
                for anode in openlis:
                    if anode.node == node:
                        flag = True
                        if curNode.f + 1 < anode.f:
                            anode.f = curNode.f + 1
                        break

                if not flag:
                    #temp.append(AStarNode(node, curNode.f + 1, envir.heuri(node)))
                    openlis.append(AStarNode(node, curNode.f + 1, envir.heuri(node, a, b, c)))
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
    # Backtracking all the previous moves to reach this goal state
    while pointer:
        path.insert(0, pointer)
        pointer = pointer.prev_node
    # And print them out
    # for p in path:
    #     print(p.action)
    return path
