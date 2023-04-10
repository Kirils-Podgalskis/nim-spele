class Node:
    def __init__(self, state:list, player):
        self.state = state # The current game state
        self.player = player # The player who will make the next move
        self.children = [] # The list of child nodes
        self.move = [] # The move that led to this state
        self.minimax_value = None

    def add_child(self, node):
        self.children.append(node)

    def is_leaf(self):
        return not bool(self.children)

    def is_max_player(self):
        return self.player == "Max"

    def is_min_player(self):
        return self.player == "Min"

    def get_nim_sum(self):
        nim_sum = self.state[0] ^ self.state[1] ^ self.state[2]
        return nim_sum
    
    def eval(self):
        nim_sum = self.state[0]
        for i in range(1, len(self.state)):
            nim_sum = nim_sum ^ self.state[i]
        return nim_sum
    
    def __str__(self):
        state_str = f"State: {self.state}, Player: {self.player}, NimSum: {self.eval()}"
        children_str = ""
        for child in self.children:
            children_str += str(child) + "\n"
        return state_str + "\n" + children_str
