class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


# for DFS
class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add_node(self, node):
        self.frontier.append(node)

    def is_empty(self):
        return len(self.frontier) == 0

    def contains_state (self, state):
        return any(node.state == state for node in self.frontier)

    def remove_node(self):
        if self.is_empty():
            raise Exception("The stack frontier is empty")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[: -1]
            return node


#for BFS
class QueueFrontier(StackFrontier):
    def remove_node(self):
        if self.is_empty():
            raise Exception("The queue frontier is empty")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


class Maze():
    def __init__(self):
        ...

    def solve(self):
        #number of steps
        self.nr_steps = 0;
        
        #innitial conditions
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier() #we choose between DFS and BFS based on the type of frontier - in this case is DFS
        frontier.add_node(start)
        
        # initialize an empty visited set
        self.visited = set()

        #search
        while True:
            if frontier.is_empty:
                raise Exception("No solution")
            
            node = frontier.remove_node()
            self.nr_steps += 1

            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent != None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent

                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            self.visited.add(node.state)

            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and node.state not in self.visited:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add_node(child)




