import pygame

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 800
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
FPS = 60
BACKGROUND_COLOR = (0, 55, 0)
SPACESHIP_WIDTH = 75
SPACESHIP_HEIGHT = 75

class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ship_img = None
    
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
    def get_width(self):
        return self.ship_img.get_width()
    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ship_img = pygame.transform.scale(pygame.image.load('spaceship.png'), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
        self.mask = pygame.mask.from_surface(self.ship_img)

    def draw(self, window):
        super().draw(window)



def init_game():
    clock = pygame.time.Clock()
    player = Player(350, 650)
    player_vel = 5
    run = True
    while run:
        clock.tick(FPS)
        background = pygame.transform.scale(pygame.image.load('background_image.jpeg'), (WINDOW_WIDTH, WINDOW_HEIGHT))
        WINDOW.blit(background, (0,0))
        player.draw(WINDOW)
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() < WINDOW_HEIGHT:
            player.y += player_vel 
        if keys[pygame.K_LEFT] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WINDOW_WIDTH:
            player.x += player_vel
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

def render_window():
    pygame.init()
    pygame.display.set_caption("Project 2")
    clock = pygame.time.Clock()
    run = True

    # custom_font = pygame.font.Font("Electric-safety-Regular.ttf")

    while run:
        clock.tick(FPS)
        WINDOW.fill(BACKGROUND_COLOR)
        surface = pygame.display.get_surface()
        main_menu_font = pygame.font.SysFont("Arial", 35) 
        title_pos = (WINDOW_WIDTH // 2 - 70, WINDOW_HEIGHT // 2 - 100)
        instruction_pos = (WINDOW_WIDTH//2 - 150, WINDOW_HEIGHT//2 - 50)
        title = main_menu_font.render("Project 2", 1, "white")
        instruction = main_menu_font.render("Click anywhere to start", 1, "white")
        surface.blit(title, title_pos)
        surface.blit(instruction, instruction_pos)
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
