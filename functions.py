# TODO: delete redundancies, boilertplate and idiotic code
from node import Node
def generate_children(node:Node, depth:int):
    if depth !=0:
        for pile_idx in range(len(node.state)):
            pile = node.state[pile_idx]
            if pile > 0:
                for stones in range(1,pile+1):
                    if node.is_max_player():
                        new_state = node.state.copy()
                        new_state[pile_idx] -= stones
                        new_node = Node(new_state, "Min")
                        node.add_child(new_node)
                        generate_children(new_node, depth-1)
                    else:
                        new_state = node.state.copy()
                        new_state[pile_idx] -= stones
                        new_node = Node(new_state, "Max")
                        node.add_child(new_node)
                        generate_children(new_node, depth-1)
    else :
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

def get_human_move(piles:list):
    valid_move = False
    while not valid_move:
        pile_idx = int(input("Enter the index of the pile you want to remove stones from (0, 1, or 2): "))
        if pile_idx < 0 or pile_idx > 2:
            print("Invalid pile index. Please enter a valid index.")
            continue
        if piles[pile_idx] == 0:
            print("The selected pile is already empty. Please select another pile.")
            continue
        num_stones = int(input(f"Enter the number of stones you want to remove from pile {pile_idx}: "))
        if num_stones < 1 or num_stones > piles[pile_idx]:
            print("Invalid number of stones. Please enter a valid number.")
            continue
        valid_move = True
    return [pile_idx, num_stones]

def play_game():
    piles = [2,3,2]  # Starting piles
    player = "human"  # Human goes first

    while True:
        print(f"\nCurrent state: {piles}")
        
        if player == "human":
            while True:
                pile_idx = int(input("Enter pile index (1, 2, or 3): "))-1
                if 0 <= pile_idx < 3 and piles[pile_idx] > 0:
                    break
                else:
                    print("Invalid pile index or pile is empty, try again.")

            while True:
                stones = int(input("Enter number of stones to take: "))
                if 1 <= stones <= piles[pile_idx]:
                    break
                else:
                    print(f"Invalid number of stones, must be between 1 and {piles[pile_idx]}, try again.")

            piles[pile_idx] -= stones
            player = "computer"
        else:
            print("Computer is thinking...")
            root_node = Node(piles, "Max")
            generate_children(root_node, depth=2)
            best_choise = minimax(root_node, depth=2, is_max=True)
            print(f"Computer move: {root_node.state} -> {root_node.move}, its advantage: {best_choise}")
            piles = root_node.move
            player = "human"

        if all(p == 0 for p in piles):
            if player == "human":
                print("Computer wins!")
            else:
                print("You win!")
            break
