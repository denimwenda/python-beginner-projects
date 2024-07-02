import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BASKET_WIDTH, BASKET_HEIGHT = 100, 50
EGG_WIDTH, EGG_HEIGHT = 40, 50
BASKET_SPEED = 10
EGG_DROP_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Egg Catcher")

# Load images
basket_image = pygame.Surface((BASKET_WIDTH, BASKET_HEIGHT))
basket_image.fill(BLACK)
egg_image = pygame.Surface((EGG_WIDTH, EGG_HEIGHT))
egg_image.fill(RED)

# Basket class
class Basket:
    def __init__(self):
        self.rect = basket_image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10))
        self.speed = BASKET_SPEED
        
        def move(self, dx):
            self.rect.x += dx
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
                
        def draw(self):
            screen.blit(basket_image, self.rect.topleft)
            
            
# Egg class
class Egg:
    def __init__(self):
        self.rect = egg_image.get_rect(midtop=(random.randint(0, WIDTH - EGG_WIDTH), 0))
        self.speed = EGG_DROP_SPEED
        
    def drop(self):
        self.rect.y += self.speed
        
    def draw(self):
        screen.blit(egg_image, self.rect.topleft)
        
        
# Main game function
def main():
    clock = pygame.time.Clock()
    basket = Basket()
    eggs = []
    score = 0
    font = pygame.font.SysFont(None, 36)
    
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket.move(-BASKET_SPEED)
        if keys[pygame.K_RIGHT]:
            basket.move(BASKET_SPEED)

        if random.random() < 0.02:  # 2% chance per frame to drop a new egg
            eggs.append(Egg())

        screen.fill(WHITE)
        
        Basket.draw(screen)
        
        for egg in eggs[:]:
            egg.drop()
            egg.draw()
            if egg.rect.bottom > HEIGHT:
                eggs.remove(egg)
            elif egg.rect.colliderect(basket.rect):
                score += 1
                eggs.remove(egg)
        
        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()