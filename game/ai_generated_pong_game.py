import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # If the ball hits the left or right side of the screen,
        # reverse the x direction
        if self.rect.x <= 0 or self.rect.x >= 600:
            self.change_x *= -1

        # If the ball hits the top of the screen,
        # reverse the y direction
        if self.rect.y <= 0:
            self.change_y *= -1
            
        # If the ball hits the bottom of the screen, end the game     
        if self.rect.y >= 400:
            pygame.quit()

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
    def update(self):
        # Get the current mouse position. This returns the position
        pos = pygame.mouse.get_pos()
        # Set the left side of the paddle to the mouse position
        self.rect.x = pos[0] - self.rect.width / 2
        # Make sure the paddle doesn't move off the screen
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 600 - self.rect.width:
            self.rect.x = 600 - self.rect.width
            
pygame.init()
screen = pygame.display.set_mode([600, 400])
pygame.display.set_caption('Pong')
# Enable this to make the mouse disappear when over our window
pygame.mouse.set_visible(0)
# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)
# Create a surface we can draw on
background = pygame.Surface(screen.get_size())

# Create sprite lists for each sprite. Add a player and a ball to their respective lists.
balls = pygame.sprite.Group()
paddles = pygame.sprite.Group()

ball = Ball()
balls.add(ball)

paddle = Paddle(WHITE, 75, 15)
paddles.add(paddle)

paddle.rect.x = 300
paddle.rect.y = 390

ball.rect.x = 345
ball.rect.y = 195

ball.change_x = random.randint(-5,5)
ball.change_y = random.randint(-5,5)
clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True       
    screen.fill(BLACK)
    paddles.update()
    balls.update()

    if pygame.sprite.spritecollide(paddle, balls, False):
      ball.change_y *= -1
      
    paddles.draw(screen)
    balls.draw(screen)
    clock.tick(40)
    pygame.display.flip()

pygame.quit()
