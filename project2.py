import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
FPS = 60
BACKGROUND_COLOR = (0, 55, 0)


def render_window():
    pygame.init()
    pygame.display.set_caption("Project 2")
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        WINDOW.fill(BACKGROUND_COLOR)
        surface = pygame.display.get_surface()
        main_menu_font = pygame.font.SysFont("Arial", 35) 
        title_pos = (WINDOW_WIDTH // 2 - 70, WINDOW_HEIGHT // 2 - 100)
        instruction_pos = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 200)
        title = main_menu_font.render("Project 2", 1, "white")
        surface.blit(title, title_pos)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                init_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                init_game()


def main():
    render_window()

if __name__ == "__main__":
    main()
