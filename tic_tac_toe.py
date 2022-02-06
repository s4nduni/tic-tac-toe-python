# Tic Tac Toe Game in Python
# Author: S4nduni
# GitHub:


# Global variables.
board_list = [" "] * 9


# Details of the game.
print("\tTic Tac Toe\n")


def print_board() -> None:
    """
    Print game broad.
    """
    print(f" {board_list[0]} | {board_list[1]} | {board_list[2]} ")
    print("---+---+---")
    print(f" {board_list[3]} | {board_list[4]} | {board_list[5]} ")
    print("---+---+---")
    print(f" {board_list[6]} | {board_list[7]} | {board_list[8]} ")


def fp_input() -> None:
    """
    First player inputs.
    """
    while True:
        fp = int(input("Enter first player input: "))
        if board_list[fp - 1] == " " and fp <= 9 and fp > 0:
            board_list[fp - 1] = "X"
            break


def sp_input() -> None:
    """
    Second player inputs.
    """
    while True:
        sp = int(input("Enter second player input: "))
        if board_list[sp - 1] == " " and sp <= 9 and sp > 0:
            board_list[sp - 1] = "O"
            break


def check_winner() -> str:
    """
    Check the winner.

    Returns:
        str: First player  --> X
             Second player --> O
             Empty space   --> " "
    """
    winn_patterns = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for pattern in winn_patterns:
        if (
            board_list[pattern[0]]
            == board_list[pattern[1]]
            == board_list[pattern[2]]
            == "X"
        ):
            return "X"
        elif (
            board_list[pattern[0]]
            == board_list[pattern[1]]
            == board_list[pattern[2]]
            == "O"
        ):
            return "O"
    return " "


def run() -> None:
    """
    If the check_winner() fuction is not empty, then store the input in the board.
    First player  --> four chances.
    Second player --> five chances.
    """
    for i in range(0, 9, 1):
        if check_winner() != " ":
            break
        if i % 2 == 0:
            fp_input()
            print_board()
        else:
            sp_input()
            print_board()


def print_winner() -> None:
    """
    Print winner statement or draw statement.
    """
    if check_winner() == "X":
        print("First player is winner!")
    elif check_winner() == "O":
        print("Second player is winner!")
    else:
        print("Draw!")


def main() -> None:
    """
    The main() function.
    """
    run()
    print_winner()


if __name__ == "__main__":
    main()
