import pygame
pygame.init()

WIDTH, HEIGHT = 640, 640
SQ_SIZE = WIDTH // 8

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

def draw_board(WIN):
    WIN.fill(WHITE)
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 1:
                pygame.draw.rect(WIN, GRAY, (col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def main():
    running = True
    clock  = pygame.time.Clock()

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_board(WIN)
        pygame.display.update()
    
    pygame.quit()


main()