import pygame
pygame.init()

WIDTH, HEIGHT = 640, 640
SQ_SIZE = WIDTH // 8

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# board colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

PIECES = {}

def draw_board(WIN):
    WIN.fill(WHITE)
    for row in range(8):
        for col in range(8):
            # fill gray only the squares that has odd (row + col)
            if (row + col) % 2 == 1:
                pygame.draw.rect(WIN, GRAY, (col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

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
        PIECES[piece] = pygame.transform.scale(pygame.image.load(f"../images/{piece}.png"), (SQ_SIZE, SQ_SIZE))

def draw_pieces(WIN, board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != "--":
                WIN.blit(PIECES[piece], (col*SQ_SIZE, row*SQ_SIZE))



def main():
    running = True
    clock  = pygame.time.Clock()
    board = create_board()
    load_images()

    while running:
        # FPS controller
        clock.tick(60)

        for event in pygame.event.get():
            # pygame.QUIT is the close window button
            if event.type == pygame.QUIT:
                running = False
        
        draw_board(WIN)
        draw_pieces(WIN, board)
        pygame.display.update()


    
    pygame.quit()





main()