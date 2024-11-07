# Chess board limits
LETTERS = "abcdefgh"
NUMBERS = "12345678"

def is_valid_position(pos):
    """Check if a position is within the chess board boundaries."""
    return len(pos) == 2 and pos[0] in LETTERS and pos[1] in NUMBERS

def get_possible_moves_knight(position):
    """Generate all possible moves for a knight from the given position."""
    row, col = LETTERS.index(position[0]), int(position[1]) - 1
    moves = [
        (row + 2, col + 1), (row + 2, col - 1), (row - 2, col + 1), (row - 2, col - 1),
        (row + 1, col + 2), (row + 1, col - 2), (row - 1, col + 2), (row - 1, col - 2)
    ]
    return {f"{LETTERS[r]}{c + 1}" for r, c in moves if 0 <= r < 8 and 0 <= c < 8}

def get_possible_moves_rook(position):
    """Generate all possible moves for a rook from the given position."""
    moves = set()
    row, col = LETTERS.index(position[0]), int(position[1]) - 1
    # Add horizontal and vertical moves
    moves.update(f"{LETTERS[row]}{n + 1}" for n in range(8) if n != col)
    moves.update(f"{LETTERS[r]}{col + 1}" for r in range(8) if r != row)
    return moves

def get_white_piece():
    """Prompt the user to input the white piece and validate the input."""
    while True:
        white_input = input("Enter your white piece and position (knight/rook), e.g., 'knight a5': ").strip().lower()
        try:
            white_piece, white_pos = white_input.split()
            if white_piece not in ("knight", "rook") or not is_valid_position(white_pos):
                raise ValueError("Invalid piece or position format.")
            return white_piece, white_pos
        except ValueError:
            print("Invalid input. Please enter as 'piece position', e.g., 'knight a5'.")

def get_black_pieces():
    """Prompt the user to input black pieces one by one and validate each input."""
    black_pieces = {}
    while True:
        black_input = input("Enter black piece and position (e.g., 'pawn d4') or 'done' to finish: ").strip().lower()
        if black_input == "done":
            if len(black_pieces) >= 1:
                break
            else:
                print("You must enter at least one black piece before finishing.")
                continue

        try:
            black_piece, black_pos = black_input.split()
            if not is_valid_position(black_pos):
                raise ValueError("Invalid position format.")
            if black_pos in black_pieces:
                print(f"Position {black_pos} is already occupied by another black piece.")
                continue
            black_pieces[black_pos] = black_piece
            print(f"Black piece '{black_piece}' added at position {black_pos}.")
        except ValueError:
            print("Invalid input. Please enter as 'piece position', e.g., 'pawn d4'.")
    return black_pieces

def main():
    white_piece, white_pos = get_white_piece()
    black_pieces = get_black_pieces()

    # Determine captureable black pieces
    if white_piece == "knight":
        possible_moves = get_possible_moves_knight(white_pos)
    elif white_piece == "rook":
        possible_moves = get_possible_moves_rook(white_pos)

    # List out which black pieces can be taken
    capturable = {pos: piece for pos, piece in black_pieces.items() if pos in possible_moves}
    
    # Print the result
    if capturable:
        print("The white piece can capture the following black pieces:")
        for pos, piece in capturable.items():
            print(f"- {piece} at {pos}")
    else:
        print("No black pieces can be captured by the white piece.")

if __name__ == "__main__":
    main()
