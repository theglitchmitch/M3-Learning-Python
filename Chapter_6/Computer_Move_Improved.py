def computer_move(board, computer, human):
    """Make computer move."""
    # make a copy to work with since function will be changing list
    board = board[:]

    # the best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    WEAK_SPOT = ((2, 6), (0, 8))
    BEST_WEAK = (1, 3, 5, 7)
    print("I shall take square number", end=" ")

    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY

    # if human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY

    #computer weak spot prevention
    for row in WEAK_SPOT:
        if board[row[0]] == board[row[1]] == human:
            for move in BEST_WEAK:
                print(move)
                return move
        #done checking this move, undo it
        board[move] = EMPTY


    # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move