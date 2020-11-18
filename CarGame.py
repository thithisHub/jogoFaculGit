import pygame

pygame.init()
window_width = 1100
window_height = 700


game_display = pygame.display.set_mode((window_width, window_height))
fundo = pygame.Surface((1100,700))
fundo.fill(pygame.Color(0,100,10))
pygame.display.set_caption("Running Over Holes")


clock = pygame.time.Clock()
car_running = pygame.image.load("car_running.png")
car_running = pygame.transform.scale(car_running, (180 , 115))

rua = pygame.image.load("asfalto2.0.png")
rua = pygame.transform.scale(rua,(1110,500))

divisoria = pygame.image.load("divisoria.png")
divisoria = pygame.transform.scale(divisoria,(1100,15))


superficieDivisoria = pygame.Surface((1100,15))
superficieDivisoria.blit(divisoria,(0,0))

superficieDivisoriaBaixo = pygame.Surface((1100,15))
superficieDivisoriaBaixo.blit(divisoria,(0,0))

estrada = pygame.Surface((1100,500))
estrada.blit(rua,(0,0))

def car(x, y):
    game_display.blit(car_running, (x, y))


def game_loop():
    y_carro= 115     
    running = True
    posicaoEstrada = 0
    posicaoEstrada2 = 1099
    
    FPS =60
    while running:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()         
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                  y_carro -= 172
                if event.key == pygame.K_DOWN:
                    y_carro += 172             
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            
        
        game_display.blit(fundo,(0,0))
        posicaoEstrada -= 5
        if posicaoEstrada <= -1099:
            posicaoEstrada = 1099
        game_display.blit(estrada,(posicaoEstrada,100))
        posicaoEstrada2 -= 5
        if posicaoEstrada2 <= -1099:
            posicaoEstrada2 = 1099
        game_display.blit(estrada,(posicaoEstrada2,100))
        
        game_display.blit(superficieDivisoria,(0,100))
        game_display.blit(superficieDivisoria,(0,100))
        game_display.blit(superficieDivisoriaBaixo,(0,585))
        game_display.blit(superficieDivisoriaBaixo,(0,585))
        
                
        car(0, y_carro)

        
        pygame.display.update()
        clock.tick(FPS)

game_loop()
pygame.quit()