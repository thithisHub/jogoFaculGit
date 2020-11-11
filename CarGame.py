import pygame

pygame.init()
window_width = 1100
window_height = 700


game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Running Over Holes")


clock = pygame.time.Clock()
car_running = pygame.image.load("car_running.png")
rua = pygame.image.load("asfalto2.0.png")
divisoria = pygame.image.load("divisoria.png")
faixa = pygame.image.load("faixa.png")

superficieFaixa = pygame.Surface((1100,15))
superficieFaixa2 = pygame.Surface((1100,15))
superficieDivisoria = pygame.Surface((1100,15))
divisoria = pygame.transform.scale(divisoria,(1100,15))
superficieDivisoria.blit(divisoria,(0,0))
superficieFaixa.blit(faixa,(0,0))
superficieFaixa2.blit(faixa,(0,0))
car_running = pygame.transform.scale(car_running, (180 , 115))
rua = pygame.transform.scale(rua,(1100,500))
estrada = pygame.Surface((1100,500))
estrada.blit(rua,(0,0))

def car(x, y):
    game_display.blit(car_running, (x, y))

FPS = 60
def game_loop():
    car_width = 64
    x_change = 0
    x = (window_width * 0.09)
    y = (window_height * 0.2)
    running = True
    posicaoEstrada = 0
    posicaoEstrada2 = 1100
    posicaoFaixa = 0
    posicaoFaixa2 = 1100
    while running:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            
        x += x_change
        
        game_display.blit(estrada,(posicaoEstrada,100))
        game_display.blit(estrada,(posicaoEstrada2,100))
        game_display.blit(divisoria,(0,100))
        estrada.blit(superficieFaixa,(posicaoFaixa,235))
        estrada.blit(superficieFaixa2,(posicaoFaixa2,235))
        posicaoEstrada -= 3
        posicaoFaixa -= 2
        if posicaoFaixa <= -1100:
            posicaoFaixa  = 1100
        posicaoFaixa2 -= 2
        if posicaoFaixa2 <= -1100:
            posicaoFaixa2  = 1100  
        if posicaoEstrada <= -1100:
            posicaoEstrada = 1100
        posicaoEstrada2 -= 3
        if posicaoEstrada2 <= -1100:
            posicaoEstrada2 = 1100
        
        car(x, 115)

        if x < 0 or x > (window_width - car_width):
            running = False
            print("You Carshed!!!!")

        pygame.display.update()
        clock.tick(FPS)

game_loop()
pygame.quit()