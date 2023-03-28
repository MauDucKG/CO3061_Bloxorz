import math
import random
import sys
import time
from ultis import *

class MCTSnode:
    def __init__(self, node: Node, parent = None):
        self.node = node
        self.parent = parent
        self.children = []
        self.g = 0
        if parent:
            self.g = parent.g + 1
        self.visits = 0
        self.value = 0.0
        self.end = False
    
    def expand(self, envir: State, root):
        # Tạo ra các nút con để mở rộng cây tìm kiếm.
        envir.set_player_position(self.node)
        nextNodes = envir.next_position(self.node)

        # kiểm tra xem node đã có trên cây chưa
        for node in nextNodes:
            oldNode = root.is_contain(node)
            """if oldNode:
                if self.g + 1 < oldNode.g:
                    oldNode.parent.removeChild(oldNode)
                    self.children.append(MCTSnode(node, self))
            else:
                self.children.append(MCTSnode(node, self))"""
            if not oldNode:
                self.children.append(MCTSnode(node, self))
    
    def is_leaf(self):
        # Kiểm tra xem nút hiện tại có phải là nút lá hay không.
        return not self.children
    
    def rollout(self, envir: State, root, maxstep = 30):
        if not self.is_leaf():
            raise ValueError("Node is not a leaf.")

        # Thực hiện quá trình rollout
        current_state = self.node
        #closelis = root.visitedNode()
        closelis = []

        for i in range(maxstep):
            # Lấy danh sách các nước đi tiếp theo từ trạng thái hiện tại
            closelis += [current_state]
            envir.set_player_position(current_state)
            if envir.check_goal():
                return sys.maxsize
            
            nextNodes = envir.next_position(current_state)
            validNode = []
            for node in nextNodes:
                if node not in closelis:
                    validNode.append(node)

            if not validNode:
                return 0

            # Thực hiện nước đi được chọn và chuyển đổi trạng thái hiện tại
            current_state = random.choice(nextNodes)

        # Trả về kết quả của trạng thái cuối cùng
        return 100 - envir.heuri(current_state)
    
    def backpropagate(self, value, visit = 1):
        # Cập nhật thông tin của các nút cha trên đường đi từ nút hiện tại đến nút gốc.
        self.visits += visit
        self.value += value
        if self.parent:
            self.parent.backpropagate(value)
    
    def uct_value(self, total_visits, exploration_value = 2):
        # Tính giá trị UCT (Upper Confidence Bound for Trees) cho nút hiện tại.
        if self.end:
            return - float("inf")
        elif self.visits == 0:
            return float("inf")
        return self.value / self.visits + exploration_value * math.sqrt(math.log(total_visits) / self.visits)

    def is_exist(self, mnode):
        if self.node == mnode.node:
            return True

        for childNode in mnode.children:
            if self.is_exist(childNode):
                return True

        return False

    def is_contain(self, node: Node):
        if not node:
            return None

        if self.node == node:
            return self
        for child in self.children:
            findNode = child.is_contain(node)
            if findNode:
                return findNode
            
        return None

    def getSize(self):
        return sys.getsizeof(self) + sum(child.getSize() for child in self.children)

    def visitedNode(self):
        nodelis = [self.node]
        for child in self.children:
            nodelis += child.visitedNode()
        return nodelis

    def removeChild(self, child):
        self.children.remove(child)
        self.backpropagate(child.value, 0)

    def checking_end(self):
        if self.end == True:
            return True
        
        for child in self.children:
            if not child.end:
                self.end = False
                return False

        if self.visits < 2 and self.children == []:
            self.end = False
            return False
        else:
            self.end = True
            if self.parent:
                self.parent.checking_end()
            return True


def monteTreeSearch(envir: State, exploration_value = 2, maxstep = 30, time_limit = 60):
    root = MCTSnode(envir.start)
    nNode = 0
    curNode = root
    
    if time_limit is not None:
        end_time = time.time() + time_limit
    
    while True:
        nNode += 1 
        curNode = root

        # Selection phase
        while not curNode.is_leaf():
            total_visits = sum(child.visits for child in curNode.children)
            uct_values = [child.uct_value(total_visits, exploration_value) for child in curNode.children]
            selected_index = uct_values.index(max(uct_values))
            curNode = curNode.children[selected_index]
        
        #print("roll out at: ", curNode.node)
        envir.set_player_position(curNode.node)
        if envir.check_goal():
            break

        # Expansion phase
        if curNode.visits > 0:
            curNode.expand(envir, root)
            #for child in curNode.children:
                #print("|   leaf: ", child.node)
            if not curNode.children:
                curNode.backpropagate(0)
                curNode.checking_end()
            else:
                curNode = random.choice(curNode.children)
                rollout_value = curNode.rollout(envir, root)
                curNode.backpropagate(rollout_value)
        else:
            # Rollout phase
            rollout_value = curNode.rollout(envir, root)
        
            # Backpropagation phase
            curNode.backpropagate(rollout_value)
        
        # Check time limit
        if time_limit is not None and time.time() > end_time:
            break
    
    pointer = curNode.node
    path = []
    while pointer:
        path.insert(0, pointer)
        pointer = pointer.prev_node

    return path, nNode, root.getSize()
