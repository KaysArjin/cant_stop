class CantStopGame:
    def __init__(self):
        self.board_columns = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # Columns in the game
        self.board = self.initialize_board()
        self.players = self.initialize_players()
    
    def initialize_board(self):
        # Initialize the board with the number of spaces each column needs
        # Note: Columns 2 and 12 have 3 spaces, 3 and 11 have 5 spaces, and so on
        board = {column: 0 for column in self.board_columns}
        return board

    def initialize_players(self):
        # Initialize two players with a dictionary that tracks their progress on each column
        players = {player_id: {column: 0 for column in self.board_columns} for player_id in range(2)}
        return players

    def display_board(self):
        # Display the current state of the board and player progress
        print("Board State:")
        for column in self.board_columns:
            print(f"Column {column}: {self.board[column]} spaces")

        print("\nPlayer Progress:")
        for player_id, progress in self.players.items():
            print(f"Player {player_id}:")
            for column, position in progress.items():
                print(f"Column {column}: {position} progress")
    
def main():
    game = CantStopGame()
    game.display_board()

if __name__ == "__main__":
    main()
