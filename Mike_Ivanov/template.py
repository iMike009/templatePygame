# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import os

# Настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder,'robot.png'))

game_folder2 = os.path.dirname(__file__)
img_folder2 = os.path.join(game_folder2, 'img')
bot_img = pygame.image.load(os.path.join(img_folder2,'zombie.png'))


WIDTH = 720 # Ширина игрового окна
HEITH = 480 # Высота игрового окна
FPS = 30 # Частота кадров в секунду

# Цвета
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEITH / 2)
    
    def update(self):
        self.rect.x +=5
        if self.rect.left > WIDTH:
            self.rect.right = 0

class Bot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bot_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEITH / 2)
    
    def update(self):
        self.rect.y -=5
        if self.rect.top == HEITH:
             self.rect.y +=5

# Создаём окно игры
pygame.init
pygame.mixer.init
screen = pygame.display.set_mode((WIDTH,HEITH))
pygame.display.set_caption('Шаблон') # Название игры
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
bot = Bot()
all_sprites.add(player)
all_sprites.add(bot)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод событий
    for event in pygame.event.get():
        # Проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
    # Обновление
    all_sprites.update()
    #Рендеринг(Отрисовка)
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()


pygame.quit()
