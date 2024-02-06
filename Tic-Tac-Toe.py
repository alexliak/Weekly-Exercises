import random  # Import the random module to use random features

class TicTacToe:
    def __init__(self, user_name):
        self.user_name = user_name  # Get the user's name as input
        self.computer_name = "Computer"  # Set the computer's name
        self.board = [['-' for _ in range(3)] for _ in range(3)]  # Initialize 3x3 board with '-'
        self.current_player = 'X'  # User plays as 'X'
        self.computer_player = 'O'

    def display_board(self):
        for row in self.board:
            print(' '.join(row))
        print()  # Add an extra newline for better readability

    def play(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position. Row and column must be between 0 and 2.")
            return False
        elif self.board[row][col] != '-':
            print("Position already taken. Choose another.")
            return False
        else:
            self.board[row][col] = self.current_player  # Set the user's or computer's mark on the board
            return True

    def get_winner(self):
        # Check rows, columns, and diagonals for a winner
        lines = self.board + list(zip(*self.board))  # Rows and columns
        lines.append([self.board[i][i] for i in range(3)])  # Diagonal top-left to bottom-right
        lines.append([self.board[i][2-i] for i in range(3)])  # Diagonal top-right to bottom-left

        for line in lines:
            if line.count(line[0]) == 3 and line[0] != '-':
                return line[0]
        return None

    def is_tie(self):
        if any('-' in row for row in self.board):
            return False
        return self.get_winner() is None

    def computer_move(self):
        # Find empty cells on the board
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == '-']
        return random.choice(empty_cells)  # Randomly select an empty cell for the computer's move

    def reset(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

def main():
    user_name = input("Enter your name: ")  # Get the user's name as input
    game = TicTacToe(user_name)
    
    while True:
        if game.current_player == 'X':  # User's turn
            print(f"{game.user_name}'s turn")
        else:  # Computer's turn
            print(f"{game.computer_name}'s turn")
        
        game.display_board()
        
        if game.current_player == 'X':
            try:
                row = int(input("Row [0-2]: "))
                col = int(input("Col [0-2]: "))
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid position. Row and column must be between 0 and 2.")
                    continue  # Retry without changing the player
                if not game.play(row, col):
                    continue  # Invalid move, retry without changing the player
            except ValueError:
                print("Please enter numbers only.")
                continue
        else:  # Computer's turn
            row, col = game.computer_move()  # Get the computer's move
            print(f"{game.computer_name} chooses row {row} and column {col}")
            if not game.play(row, col):
                continue  # Retry without changing the player
        
        # Check for a winner or tie
        winner = game.get_winner()
        if winner:
            game.display_board()
            if winner == 'X':
                print(f"{game.user_name} wins!")
            else:
                print(f"{game.computer_name} wins!")
            break  # Exit the game loop when there's a winner
        elif game.is_tie():
            game.display_board()
            print("It's a tie!")
            break  # Exit the game loop when it's a tie

        # Switch players
        game.current_player = 'X' if game.current_player == 'O' else 'O'

if __name__ == "__main__":
    main()
