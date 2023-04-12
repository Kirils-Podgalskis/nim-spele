from node import Node

# function, that generates the children of a current state in the game tree
def generate_children(node:Node, depth:int):
    if depth !=0:
        for pile_idx in range(len(node.state)):
            pile = node.state[pile_idx]
            if pile > 0:
                for stones in range(1,pile+1):
                    new_state = node.state.copy()
                    new_state[pile_idx] -= stones
                    if node.is_max_player(): new_node = Node(new_state, "Min")
                    else: new_node = Node(new_state, "Max")
                    node.add_child(new_node)
                    generate_children(new_node, depth-1)
    else:
        return

# minimax algorithm, that returns the best move for the current state
def minimax(node:Node, is_max:bool):
    if node.is_leaf():
        return node.eval()

    # max player, that tries to maximize chances of winning by choosing the move value as close to 0 as possible
    if is_max:
        best_value = -float("inf")
        for child in node.children:
            child.minimax_value = minimax(child, False)
            # if the child is a winning state, return the value of the child and end the search
            # this is called alpha-beta pruning, although it is the only pruning in this algorithm
            if child.state == [0,0,0]:
                best_value = child.minimax_value
                best_child = child
                node.move = best_child.state
                return best_value
            if child.minimax_value > best_value:
                best_value = child.minimax_value
                best_child = child
        node.move = best_child.state
        return best_value
    # min player, that tries to minimize max player's chances of winning by choosing the move value as far from 0 as possible
    else:
        best_value = float("inf")
        for child in node.children:
            child.minimax_value = minimax(child, True)
            if child.minimax_value < best_value:
                best_value = child.minimax_value
                best_child = child
        node.move = best_child.state
        return best_value

