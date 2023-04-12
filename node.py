class Node:
    def __init__(self, state:list, player):
        self.state = state # The current game state
        self.player = player # The player who will make the next move
        self.children = [] # The list of child nodes
        self.move = [] # hold the best move for the current state
        self.minimax_value = None # The minimax value of this node that is assigned by the minimax algorithm

    # Adds a child node to the current node
    def add_child(self, node):
        self.children.append(node)

    # Returns true if the current node is a leaf node
    def is_leaf(self):
        return not bool(self.children)

    # Returns true if the current node is a max node
    def is_max_player(self):
        return self.player == "Max"

    # Returns true if the current node is a min node
    def is_min_player(self):
        return self.player == "Min"

    # Returns the nim sum of the current state
    def eval(self):
        nim_sum = self.state[0] ^ self.state[1] ^ self.state[2]
        return nim_sum
    
    # prints the current state and all of its children, used for debugging
    def __str__(self):
        state_str = f"State: {self.state}, Player: {self.player}, NimSum: {self.eval()}"
        children_str = ""
        for child in self.children:
            children_str += str(child) + "\n"
        return state_str + "\n" + children_str
