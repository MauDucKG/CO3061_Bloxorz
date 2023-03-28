from ultis import *
import sys, time

class AStarNode:
    def __init__(self, node: Node, f, h):
        self.node = node
        self.f = f
        self.h = h

    def __lt__(self, node):
        return (self.f + self.h) < (node.f + node.h)
    
    def __eq__(self, anode) -> bool:
        return self.node == anode.node and self.f == anode.f and self.h == anode.h

def AStarSearch(envir: State, a = 4, b = 4, c = 20, time_limit = 60):
    openlis = [AStarNode(envir.start, 0, sys.maxsize)]
    closelis = []
    nNode = 0

    if time_limit is not None:
        end_time = time.time() + time_limit

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
            for anode in closelis:
                if anode.node == node:
                    flag = True
                    break
            if not flag:
                for anode in openlis:
                    if anode.node == node:
                        flag = True
                        if curNode.f + 1 < anode.f:
                            openlis.remove(anode)
                            openlis.append(AStarNode(node, curNode.f + 1, envir.heuri(node, a, b, c)))
                        break

                if not flag:
                    #temp.append(AStarNode(node, curNode.f + 1, envir.heuri(node)))
                    openlis.append(AStarNode(node, curNode.f + 1, envir.heuri(node, a, b, c)))
                    #bisect.insort_left(openlis, AStarNode(node, curNode.f + 1, envir.heuri(node)))
        
        if time_limit is not None and time.time() > end_time:
            break
                    
                

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
    mem = 0
    if openlis != []: mem += len(openlis)*sys.getsizeof(openlis[0])
    if closelis != []: mem += len(closelis)*sys.getsizeof(closelis[0])
    return path, nNode, mem
