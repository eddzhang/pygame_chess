import pygame
pygame.init()

font = pygame.font.SysFont("Arial", 20) # for words

width, height = 640, 640
SQ_SIZE = width // 8

WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess")

# board colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

PIECES = {}

def draw_board(WIN):
    WIN.fill(WHITE)

    files = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    ranks = ['8', '7', '6', '5', '4', '3', '2', '1']

    for row in range(8):
        for col in range(8):
            # fill gray only the squares that has odd (row + col)
            if (row + col) % 2 == 1:
                pygame.draw.rect(WIN, GRAY, (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

            if row == 7:
                letter = files[col]  # A, B, C...
                label = font.render(letter, True, (0, 0, 0))
                x = col * SQ_SIZE + 5
                y = height - 20
                WIN.blit(label, (x, y))

            if col == 0:
                number = ranks[row]  # 8, 7, 6...
                label = font.render(number, True, (0, 0, 0))
                x = 5
                y = row * SQ_SIZE + 5
                WIN.blit(label, (x, y))

def create_board():
    return [ ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"], # black bottom row
            ["bP"] * 8, # black pawns
            ["--"] * 8,
            ["--"] * 8,
            ["--"] * 8,
            ["--"] * 8,
            ["wP"] * 8, # white pawns
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],] # white bottom row

def load_images():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bP', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        PIECES[piece] = pygame.transform.scale(pygame.image.load(f"images/{piece}.png"), (SQ_SIZE, SQ_SIZE))

def draw_pieces(WIN, board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != "--":
                WIN.blit(PIECES[piece], (col*SQ_SIZE, row*SQ_SIZE))

def highlight_square(WIN, selected_square):
    if selected_square:
        row, col = selected_square
        highlight_color = (0, 255, 0, 100)  # green highlight

        surface = pygame.Surface((SQ_SIZE, SQ_SIZE))
        surface.set_alpha(100)
        surface.fill((0, 255, 0))
        WIN.blit(surface, (col * SQ_SIZE, row * SQ_SIZE))

def main():
    running = True
    clock  = pygame.time.Clock()
    board = create_board()
    load_images()

    selected_square = None # mouse click
    current_player = "w" # white starts

    while running:
        # FPS controller
        clock.tick(60)

        for event in pygame.event.get():
            # pygame.QUIT is the close WINdow button
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()  # x,y tuple
                col = pos[0] // SQ_SIZE # map the x coord to a col
                row = pos[1] // SQ_SIZE # map y coord to a row

                if selected_square is None:
                    # first click
                    if board[row][col] != "--" and board[row][col][0] == current_player:
                        selected_square = (row, col)
                else:
                    # second click
                    start_row, start_col = selected_square
                    piece = board[start_row][start_col]
                    target = board[row][col]

                    if target == '--' or target[0] != current_player:
                        board[row][col] = piece
                        board[start_row][start_col] = "--"
                        
                        # print the notation in console
                        files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
                        ranks = ['8', '7', '6', '5', '4', '3', '2', '1']

                        start_notation = files[start_col] + ranks[start_row]
                        end_notation = files[col] + ranks[row]

                        print(f"{piece} from {start_notation} to {end_notation}")


                        # change turns
                        if current_player == "w":
                            current_player = "b"
                        else:
                            current_player = "w"

                    selected_square = None  # reset 
        
        draw_board(WIN)
        highlight_square(WIN, selected_square)
        draw_pieces(WIN, board)
        pygame.display.update()


    
    pygame.quit()





main()