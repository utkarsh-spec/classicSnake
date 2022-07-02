import pygame
import random


pygame.init()
display = pygame.display.set_mode([500, 500])
pygame.display.set_caption("classic snake")
score = 0


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.vel = 5
        self.grow = False

    def draw(self):
        pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def move(self):
        if left:
            if self.x >= 0:
                self.x -= self.vel
            else:
                self.x = 490
        if right:
            if self.x <= 500:
                self.x += self.vel
            else:
                self.x = -5
        if up:
            if self.y >= 0:
                self.y -= self.vel
            else:
                self.y = 490
        if down:
            if self.y <= 500:
                self.y += self.vel
            else:
                self.y = -5


class Enemy:
    is_draw = True
    x = 100
    y = 100

    def draw(self):
        if self.is_draw:
            pygame.draw.rect(display, (255, 255, 255), (self.x, self.y, 10, 10))


snake = Snake(50, 50)
enemy = Enemy()


def main():
    global score
    snake.draw()
    for grow in range(score):
        if down:
            pygame.draw.rect(display, [255, 100, 100], [snake.x, snake.y - snake.height*grow, 10, 10])
        if left:
            pygame.draw.rect(display, [255, 100, 100], [snake.x + snake.width*grow, snake.y, 10, 10])
        if right:
            pygame.draw.rect(display, [255, 100, 100], [snake.x - snake.width * grow, snake.y, 10, 10])
        if up:
            pygame.draw.rect(display, [255, 100, 100], [snake.x, snake.y+snake.height*grow, 10, 10])
    caption()
    if enemy.is_draw is False:
        enemy.x = random.randrange(0, 400)
        enemy.y = random.randrange(0, 400)
        enemy.is_draw = True
    if enemy.is_draw is True:
        enemy.draw()

    if enemy.is_draw:
        if snake.x + snake.width >= enemy.x and snake.y + snake.width >= enemy.y and snake.x <= enemy.x+10 and snake.y <= enemy.y+10:
            enemy.is_draw = False
            score += 1
            snake.grow = True


def caption():
    font1 = pygame.font.SysFont('comicsans', 30)
    text1 = font1.render('score: '+str(score), True, (255, 255, 255))
    display.blit(text1, (400, 10))


right = False
left = False
up = False
down = False
run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        left = True
        right = False
        up = False
        down = False
    if key[pygame.K_RIGHT]:
        snake.x1 = snake.x
        snake.y1 = snake.y
        right = True
        left = False
        up = False
        down = False
    if key[pygame.K_UP]:
        up = True
        down = False
        left = False
        right = False
    if key[pygame.K_DOWN]:
        down = True
        up = False
        right = False
        left = False

    if right:
        snake.move()
    if left:
        snake.move()
    if up:
        snake.move()
    if down:
        snake.move()

    display.fill([0, 0, 0])
    main()
    pygame.display.update()

