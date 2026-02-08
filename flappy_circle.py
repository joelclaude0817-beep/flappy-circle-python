import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 250)
GREEN = (34, 139, 34)
RED = (255, 69, 0)
YELLOW = (255, 215, 0)

# Game variables
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_WIDTH = 70
PIPE_GAP = 200
PIPE_VELOCITY = 3
SPAWN_PIPE_EVENT = pygame.USEREVENT
PIPE_SPAWN_TIME = 2500  # milliseconds

class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.velocity = 0
        self.color = YELLOW
        
    def flap(self):
        self.velocity = FLAP_STRENGTH
        
    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        # Draw a simple eye
        eye_x = int(self.x + 7)
        eye_y = int(self.y - 5)
        pygame.draw.circle(screen, BLACK, (eye_x, eye_y), 3)
        
    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 
                          self.radius * 2, self.radius * 2)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.gap_y = random.randint(150, SCREEN_HEIGHT - 150 - PIPE_GAP)
        self.top_height = self.gap_y
        self.bottom_y = self.gap_y + PIPE_GAP
        self.bottom_height = SCREEN_HEIGHT - self.bottom_y
        self.passed = False
        
    def update(self):
        self.x -= PIPE_VELOCITY
        
    def draw(self, screen):
        # Top pipe
        pygame.draw.rect(screen, GREEN, (self.x, 0, PIPE_WIDTH, self.top_height))
        pygame.draw.rect(screen, BLACK, (self.x, 0, PIPE_WIDTH, self.top_height), 2)
        # Pipe cap
        pygame.draw.rect(screen, GREEN, (self.x - 5, self.top_height - 20, PIPE_WIDTH + 10, 20))
        pygame.draw.rect(screen, BLACK, (self.x - 5, self.top_height - 20, PIPE_WIDTH + 10, 20), 2)
        
        # Bottom pipe
        pygame.draw.rect(screen, GREEN, (self.x, self.bottom_y, PIPE_WIDTH, self.bottom_height))
        pygame.draw.rect(screen, BLACK, (self.x, self.bottom_y, PIPE_WIDTH, self.bottom_height), 2)
        # Pipe cap
        pygame.draw.rect(screen, GREEN, (self.x - 5, self.bottom_y, PIPE_WIDTH + 10, 20))
        pygame.draw.rect(screen, BLACK, (self.x - 5, self.bottom_y, PIPE_WIDTH + 10, 20), 2)
        
    def collide(self, circle):
        circle_rect = circle.get_rect()
        top_pipe_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.top_height)
        bottom_pipe_rect = pygame.Rect(self.x, self.bottom_y, PIPE_WIDTH, self.bottom_height)
        
        return circle_rect.colliderect(top_pipe_rect) or circle_rect.colliderect(bottom_pipe_rect)
    
    def off_screen(self):
        return self.x < -PIPE_WIDTH

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Circle")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 36)
        self.reset()
        
    def reset(self):
        self.circle = Circle(100, SCREEN_HEIGHT // 2)
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.started = False
        pygame.time.set_timer(SPAWN_PIPE_EVENT, PIPE_SPAWN_TIME)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.game_over:
                        self.circle.flap()
                        self.started = True
                    else:
                        self.reset()
                elif event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.game_over:
                    self.circle.flap()
                    self.started = True
                else:
                    self.reset()
            if event.type == SPAWN_PIPE_EVENT and self.started and not self.game_over:
                self.pipes.append(Pipe(SCREEN_WIDTH))
        return True
        
    def update(self):
        if not self.started or self.game_over:
            return
            
        self.circle.update()
        
        # Check if circle hits floor or ceiling
        if self.circle.y - self.circle.radius <= 0 or \
           self.circle.y + self.circle.radius >= SCREEN_HEIGHT:
            self.game_over = True
            
        # Update pipes
        for pipe in self.pipes[:]:
            pipe.update()
            
            # Check collision
            if pipe.collide(self.circle):
                self.game_over = True
                
            # Check if passed pipe
            if not pipe.passed and pipe.x + PIPE_WIDTH < self.circle.x:
                pipe.passed = True
                self.score += 1
                
            # Remove off-screen pipes
            if pipe.off_screen():
                self.pipes.remove(pipe)
                
    def draw(self):
        # Draw background
        self.screen.fill(BLUE)
        
        # Draw pipes
        for pipe in self.pipes:
            pipe.draw(self.screen)
            
        # Draw circle
        self.circle.draw(self.screen)
        
        # Draw score
        score_text = self.font.render(str(self.score), True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        self.screen.blit(score_text, score_rect)
        
        # Draw start message
        if not self.started:
            start_text = self.small_font.render("Press SPACE or Click to Start", True, WHITE)
            start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(start_text, start_rect)
            
        # Draw game over message
        if self.game_over:
            game_over_text = self.font.render("Game Over!", True, RED)
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
            self.screen.blit(game_over_text, game_over_rect)
            
            restart_text = self.small_font.render("Press SPACE to Restart", True, WHITE)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
            self.screen.blit(restart_text, restart_rect)
            
        pygame.display.flip()
        
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
