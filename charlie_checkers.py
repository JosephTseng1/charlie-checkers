import sys
import copy

#Check for valid index
def index_check(index):
    return (index >= 0 and index < 8)

#Returning the game board
def make_board():
    board = [[1,0,1,0,0,0,2,0],
             [0,1,0,0,0,2,0,2],
             [1,0,1,0,0,0,2,0],
             [0,1,0,0,0,2,0,2],
             [1,0,1,0,0,0,2,0],
             [0,1,0,0,0,2,0,2],
             [1,0,1,0,0,0,2,0],
             [0,1,0,0,0,2,0,2]]
    return board

#Printing the game board
def print_board(board):
    print("     0   1   2   3   4   5   6   7")
    print("   ---------------------------------")
    for col in range(0,8):
        print(col, end = "  | ")
        for row in range(0,8):
            if (board[row][col] == 1):
                print ("r", end = " | ")
            elif (board[row][col] == 3):
                print ("R", end = " | ")
            elif (board[row][col] == 2):
                print ("b", end = " | ")
            elif (board[row][col] == 4):
                print ("B", end = " | ")
            else:
                print (" ", end = " | ")
        print()
        print("   ---------------------------------")
    print()

#Dealing with the situation in moving up left, seeing if it's feasible
def move_up_left(x, y, board):
    if(index_check(x-1) and index_check(y-1)):
        if(board[x - 1][y - 1] == 0):
            if (y - 1 == 0 and board[x][y] <= 2):
                board[x - 1][y - 1] = board[x][y] + 2
            else:
                board[x - 1][y - 1] = board[x][y]
            board[x][y] = 0
            return True
    return False

#Dealing with the situation in moving up right, seeing if it's feasible
def move_up_right(x, y, board):
    if(index_check(x+1) and index_check(y-1)):
        if(board[x + 1][y - 1] == 0):
            if (y - 1 == 0 and board[x][y] <= 2):
                board[x + 1][y - 1] = board[x][y] + 2
            else:
                board[x + 1][y - 1] = board[x][y]
            board[x][y] = 0
            return True
    return False

#Dealing with the situation in moving down left, seeing if it's feasible
def move_down_left(x, y, board):
    if(index_check(x-1) and index_check(y+1)):
        if(board[x - 1][y + 1] == 0):
            if (y + 1 == 7 and board[x][y] <= 2):
                board[x - 1][y + 1] = board[x][y] + 2
            else:
                board[x - 1][y + 1] = board[x][y]
            board[x][y] = 0
            return True
    return False

#Dealing with the situation in moving down right, seeing if it's feasible
def move_down_right(x, y, board):
    if(index_check(x+1) and index_check(y+1)):
        if(board[x + 1][y + 1] == 0):
            if (y + 1 == 7 and board[x][y] <= 2):
                board[x + 1][y + 1] = board[x][y] + 2
            else:
                board[x + 1][y + 1] = board[x][y]
            board[x][y] = 0
            return True
    return False

#Dealing with the situation in moving up left, seeing if it's feasible
def take_up_left(x, y, board):
    if(x - 2 >= 0 and y - 2 >= 0):
        if(board[x - 1][y - 1] != 0 and board[x - 1][y - 1] % 2 != board[x][y] % 2):
            if(board[x - 2][y - 2] == 0):
                if (y - 2 == 0 and board[x][y] <= 2):
                    board[x - 2][y - 2] = board[x][y] + 2
                else:
                    board[x - 2][y - 2] = board[x][y]
                board[x - 1][y - 1] = 0
                board[x][y] = 0
                return True
    return False

#Dealing with the situation in moving up right, seeing if it's feasible
def take_up_right(x, y, board):
    if(x + 2 <= 7 and y - 2 >= 0):
        if(board[x + 1][y - 1] != 0 and board[x + 1][y - 1] % 2 != board[x][y] % 2):
            if(board[x + 2][y - 2] == 0):
                if (y - 2 == 0 and board[x][y] <= 2):
                    board[x + 2][y - 2] = board[x][y] + 2
                else:
                    board[x + 2][y - 2] = board[x][y]
                board[x + 1][y - 1] = 0
                board[x][y] = 0
                return True
    return False

#Dealing with the situation in moving down left, seeing if it's feasible
def take_down_left(x, y, board):
    if(x - 2 >= 0 and y + 2 <= 7):
        if(board[x - 1][y + 1] != 0 and board[x - 1][y + 1] % 2 != board[x][y] % 2):
            if(board[x - 2][y + 2] == 0):
                if (y + 2 == 7 and board[x][y] <= 2):
                    board[x - 2][y + 2] = board[x][y] + 2
                else:
                    board[x - 2][y + 2] = board[x][y]
                board[x - 1][y + 1] = 0
                board[x][y] = 0
                return True
    return False

#Dealing with the situation in moving down right, seeing if it's feasible
def take_down_right(x, y,board):
    if(x + 2 <= 7 and y + 2 <= 7):
        if(board[x + 1][y + 1] != 0 and board[x + 1][y + 1] % 2 != board[x][y] % 2):
            if(board[x + 2][y + 2] == 0):
                if (y + 2 == 7 and board[x][y] <= 2):
                    board[x + 2][y + 2] = board[x][y] + 2
                else:
                    board[x + 2][y + 2] = board[x][y]
                board[x + 1][y + 1] = 0
                board[x][y] = 0
                return True
    return False

#Number of safe spaces for the human player
def num_of_even_safe_spaces(board):
    safe_count = 0

    for i in range(8):
        for j in range(8):
            if board[i][j] % 2 == 0 and board[i][j] != 0:
                left_safe = True
                right_safe = True

                #checking to see if the left side is vulnerable                                 
                #to the enemy regular piece or king                                             
                if index_check(i-1) and index_check(j-1) and board[i-1][j-1] % 2 != 0:
                    if index_check(i+1) and index_check(j+1) and board[i+1][j+1] == 0:
                        left_safe = False

                #checking to see if the right side is vulnerable                                
                #to the enemy regular piece or king                                             
                if index_check(i-1) and index_check(j+1) and board[i-1][j+1] % 2 != 0:
                    if index_check(i+1) and index_check(j-1) and board[i+1][j-1] == 0:
                        right_safe = False

                if index_check(i+1) and index_check(j-1) and board[i+1][j-1] == 3:
                    if index_check(i-1) and index_check(j+1) and board[i-1][j+1] == 0:
                        left_safe = False

                #Checks to see if the piece is vulnerable to an enemy king                      
                #from the right side on the back because kings can jump backwards!              
                if index_check(i+1) and index_check(j+1) and board[i+1][j+1] == 3:
                    if index_check(i-1) and index_check(j-1) and board[i-1][j-1] == 0:
                        right_safe = False

                if (left_safe and right_safe):
                    safe_count += 1
    return safe_count

#Number of safe spaces for Charlie
def num_of_odd_safe_spaces(board):
    safe_count = 0

    for i in range(8):
        for j in range(8):
            if board[i][j] % 2 != 0:

                left_safe = True
                right_safe = True

                #checking to see if the left side is vulnerable                                
                #to the enemy regular piece or king                                             
                #down left                                                                      
                if index_check(i-1) and index_check(j+1) and board[i-1][j+1] % 2 == 0 and board[i]:
                    if index_check(i-1) and index_check(j+1) and board[i-1][j+1] == 0:
                        left_safe = False

                #checking to see if the right side is vulnerable                               
                #to the enemy regular piece or king                                            
                if index_check(i+1) and index_check(j+1) and board[i+1][j+1] % 2 == 0 and board[i]:
                    if index_check(i+1) and index_check(j+1) and board[i+1][j+1] == 0:
                        right_safe = False

                #Checks to see if the piece is vulnerable to an enemy king                     
                #from the left side on the back because kings can jump backwards!              
                if index_check(i-1) and index_check(j-1) and board[i-1][j-1] == 4:
                    if index_check(i+1) and index_check(j+1) and board[i+1][j+1] == 0:
                        left_safe = False

                #Checks to see if the piece is vulnerable to an enemy king                     
                #from the right side on the back because kings can jump backwards!             
                if index_check(i-1) and index_check(j+1) and board[i-1][j+1] == 4:
                    if index_check(i+1) and index_check(j-1) and board[i+1][j-1] == 0:
                        right_safe = False

                if (left_safe and right_safe):
                    safe_count += 1
    return safe_count

#Calculating the number of safe spaces for Charlie to make, the heuristic function
def charlie_ai_heuristic(board):
    num_of_even = 0

    for i in range(8):
        for j in range(8):
            if board[i][j] == 2 or board[i][j] == 4:
                num_of_even += 1

    if num_of_even == 0:
        return 100
    return (num_of_odd_safe_spaces(board) - num_of_even_safe_spaces(board))

# Check if syntax is right for a normal piece
def checker_move(command, board):
    return (len(command) == 4 and command[0] == "move" or command[0] == "jump" and command[1].isdigit() and command[2].isdigit() and index_check(int(command[1])) and index_check(int(command[2])) and command[3] == "upleft" or command[3] == "upright" and board[int(command[1])][int(command[2])] == 2)

# Check if syntax is right for a king piece
def king_move(command, board):
    return (len(command) == 4 and (command[0] == "move" or command[0] == "jump") and command[1].isdigit() and command[2].isdigit()
            and index_check(int(command[1])) and index_check(int(command[2])) and (command[3] == "upleft" or command[3] == "upright" or command[3] == "downleft" or command[3] == "downright")
            and board[int(command[1])][int(command[2])] == 4)

#Getting the list of child boards
def get_child_boards(board, is_charlie):
    boards = []
    
    if(is_charlie):
        parity = 1
    else:
        parity = 0

    for x in range(0,8):
        for y in range(0,8):
            if(board[x][y] != 0 and board[x][y] % 2 == parity):
                boards.extend(get_boards_from_one_pieces_takes(x, y, board))

    if (len(boards) != 0):
        return boards

    for x in range(0,8):
        for y in range(0,8):
            if(board[x][y] != 0 and board[x][y] % 2 == parity):
                boards.extend(get_boards_from_one_pieces_moves(x, y, board))
    return boards

#Determining if any pieces can be taken
def can_take(board):
    boards = []

    for x in range(0,8):
        for y in range(0,8):
            if(board[x][y] != 0 and board[x][y] % 2 == 0):
                boards.extend(get_boards_from_one_pieces_takes(x,y,board))

    if (len(boards) != 0):
        return True
    return False

#Getting the possible number of boards from one piece movies
def get_boards_from_one_pieces_moves(x, y, board):
    my_board = copy.deepcopy(board)
    child_boards = []

    if (board[x][y] != 1 and move_up_right(x, y, my_board)):
        child_boards.append(my_board)
        my_board = copy.deepcopy(board)

    if (board[x][y] != 1 and move_up_left(x, y, my_board)):
        child_boards.append(my_board)
        my_board = copy.deepcopy(board)

    if (board[x][y] != 2 and move_down_right(x, y, my_board)):
        child_boards.append(my_board)
        my_board = copy.deepcopy(board)

    if (board[x][y] != 2 and move_down_left(x, y, my_board)):
        child_boards.append(my_board)
        my_board = copy.deepcopy(board)
    return child_boards

#Getting the possible number of boards from one piece takes
def get_boards_from_one_pieces_takes(x, y, board):
    my_board = copy.deepcopy(board)
    child_boards = []

    if (board[x][y] != 1 and take_up_right(x, y, my_board)):
        child_boards.append(my_board)

        multi_takes = get_boards_from_one_pieces_takes(x+2, y-2, copy.deepcopy(my_board))
        child_boards.extend(multi_takes)

        my_board = copy.deepcopy(board)

    if (board[x][y] != 1 and take_up_left(x, y, my_board)):
        child_boards.append(my_board)

        multi_takes = get_boards_from_one_pieces_takes(x-2, y-2, copy.deepcopy(my_board))
        child_boards.extend(multi_takes)

        my_board = copy.deepcopy(board)

    if (board[x][y] != 2 and take_down_right(x, y, my_board)):
        child_boards.append(my_board)

        multi_takes = get_boards_from_one_pieces_takes(x+2, y+2, copy.deepcopy(my_board))
        child_boards.extend(multi_takes)

        my_board = copy.deepcopy(board)

    if (board[x][y] != 2 and take_down_left(x, y, my_board)):
        child_boards.append(my_board)

        multi_takes = get_boards_from_one_pieces_takes(x-2, y+2, copy.deepcopy(my_board))
        child_boards.extend(multi_takes)

        my_board = copy.deepcopy(board)
    return child_boards

#Determining if the game has been won
def game_won(board):
    charlie_moves = get_child_boards(board, True)
    human_moves = get_child_boards(board, False)

    if(len(charlie_moves) == 0 or len(human_moves) == 0):
        return True
    return False

#Determining whether or not the human wins
def human_wins(board):
    charlie_moves = get_child_boards(board, True)
    
    if(len(charlie_moves) == 0):
        return True

    human_moves = get_child_boards(board, True)

    if(len(human_moves) == 0):
        return False

#Calculating the max score in Min-Max algorithm implementation for Charlie
def max_turn(board, level, max_level):
    if(game_won(board)):
        return (-100, board)

    if (level > max_level):
        return (charlie_ai_heuristic(board),)

    is_charlie = True
    board_list = get_child_boards(board, is_charlie)

    max_score = (-101, board)
    for child_board in board_list:
        score = min_turn(child_board, level + 1, max_level)
        if( score[0] > max_score[0]):
            max_score = (score[0], child_board)
    return max_score

#Calculating the min score in Min-Max algorithm implementation for Charlie
def min_turn(board, level, max_level):
    if (game_won(board)):
        return (100, board)

    if (level > max_level):
        return (charlie_ai_heuristic(board),)

    is_charlie = False
    board_list = get_child_boards(board, is_charlie)
    min_score = (101, board)

    for child_board in board_list:
        score = max_turn(child_board, level + 1, max_level)
        if( score[0] < min_score[0]):
            min_score = (score[0], child_board)
    return min_score

#The main game loop
def game_loop(board):
    counter = 0
    double_jump = False
    print_board(board)

    while game_won(board) is False:
        error = False

        # Human's move
        if counter % 2 == 0:
            #Prompt for Human's move
            print("Enter your move:")
            command = input().strip().lower()
            command = [s.strip().lower() for s in command.split()]

            # Bad syntax or moving charlie's pieces
            error = checker_move(command, board) is False and king_move(command, board) is False
            if(error):
                print("Your move had the wrong syntax or it is not your piece.")
            else:
                move_type, x, y, direction = command[0], int(command[1]), int(command[2]), (command[3])

                # Have to jump if you can
                if (can_take(board)):
                    if (command[0] == "move"):
                        print("Please enter a jump command because you can't move if you have a capture available")
                        error = True
                    else:
                        #Dealing with error case scenarios
                        if move_type == "jump" and direction == "upleft":
                            error = not take_up_left(x, y, board)
                            if(error):
                                print("Move is illegal.")
                        elif move_type == "jump" and direction == "upright":
                            error = not take_up_right(x, y, board)
                            if(error):
                                print("Move is illegal.")
                        elif move_type == "jump" and direction == "downleft":
                            error = not take_down_left(x, y, board)
                            if(error):
                                print("Move is illegal.")
                        elif move_type == "jump" and direction == "downright":
                            error = not take_down_right(x, y, board)
                            if(error):
                                print("Move is illegal.")
                else:
                    if(command[0] == "jump"):
                        print("Please enter a move command. There are no captures available.")
                        error = True
                    else:
                        if move_type == "move" and direction == "upleft":
                            error = not move_up_left(x, y, board)
                            if(error):
                                print("Move is illegal.")
                        elif move_type == "move" and direction == "upright":
                            error = not move_up_right(x, y, board)
                            if(error):
                                print("Move is illegal.")
                        elif move_type == "move" and direction == "downleft":
                            error = not move_down_left(x, y, board)
                            if(error): 
                                print("Move is illegal.")
                        elif move_type == "move" and direction == "downright":
                            error = not move_down_right(x, y, board)
                            if(error):
                                print("Move is illegal.")
        else:
            #Charlie's turn
            print("Charlie is thinking. Please wait...")
            board = (max_turn(board, 1, 5))[1]
            print("Charlie's move:")

        # only change player and print board if no errors
        if (error == False and double_jump == False):
            counter += 1
            print_board(board)

    if human_wins(board):
        print("YOU WIN!")
    else:
        print("CHARLIE WINS!")

#Introduction
print()
print("Let's play checkers!")
print("Charlie Checkers is an AI ready to play checkers with you.")
print("On your turn type your move in the following format:")
print()
print("    moveType x y direction")
print()
print("Where moveType is eiter 'move' or 'jump',")
print("x and y are the coordinates of the piece you want to move,")
print("and direction is either 'upleft', 'upright', 'downleft', or 'downright'")
print("Good luck!")
print()

#Setting up the board
board = make_board()

#Setting up the game loop to run
game_loop(board)
