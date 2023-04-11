# TODO: delete redundancies, boilertplate and idiotic code
from node import Node
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

def minimax(node:Node, depth:int, is_max:bool):
    if depth == 0 or node.is_leaf():
        return node.get_nim_sum()

    if is_max:
        best_value = -float("inf")
        for child in node.children:
            child.minimax_value = minimax(child, depth-1, False)
            if child.minimax_value > best_value:
                best_value = child.minimax_value
                best_child = child
        node.move = best_child.state
        return best_value
    else:
        best_value = float("inf")
        for child in node.children:
            child.minimax_value = minimax(child, depth-1, True)
            if child.minimax_value < best_value:
                best_value = child.minimax_value
                best_child = child
        node.move = best_child.state
        return best_value

