import pygame
import random
import contextvars

pygame.init()
window_width = 1100
window_height = 700

arrayposicao = [115,130,215,270,375,315,415,140,240,340,420,400]
class Buraco:
    def __init__(self,posicaoPx, posicaoPy):
        self.posicaox = posicaoPx
        self.posicaoy = posicaoPy
        self.buracoimg = pygame.image.load("buraco.png")
        self.buracoimg = pygame.transform.scale(self.buracoimg,(180,130))

    def printBuraco(self,tela):
        tela.blit(self.buracoimg,(self.posicaox, self.posicaoy))
        


def car(x, y, game_display , car_running):
    game_display.blit(car_running, (x, y))


def game_loop(game_display):
    pontosFps = 0
    pontos = 0
    fonte = pygame.font.Font(None , 30)
    
    
    posicaoCarro = 0
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
    pygame.display.flip()
    
    y_carro= 115     
    running = True
    posicaoEstrada = 0
    posicaoEstrada2 = 1099
    segundosDesdeUltimoBuraco = 0
    
    FPS =60
    buracoEstrada = Buraco(1100,115)
    buracoEstrada.printBuraco(game_display)  

    buracoEstrada2 = Buraco(1100,115)
    buracoEstrada2.printBuraco(game_display) 

    buracoEstrada3 = Buraco(1100,115)
    buracoEstrada3.printBuraco(game_display) 

    buracoAtual = 0
    while running:
        fundo.fill(pygame.Color(0,100,10))
        placar = fonte.render(("Pontuação: " + str(pontos)) , (0,0) ,(255,255,255))
        pontosFps += 1
        if pontosFps % 60 == 0:
            pontos +=100
            segundosDesdeUltimoBuraco += 1
        fundo.blit(placar,(0,35))
                  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()         
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                  if posicaoCarro >= 1:
                     y_carro -= 172   
                     posicaoCarro -= 1                
                if event.key == pygame.K_DOWN:
                    if posicaoCarro <= 1:
                        y_carro += 172  
                        posicaoCarro += 1                              
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

        buracoEstrada.posicaox -= 5
        buracoEstrada2.posicaox -= 5
        buracoEstrada3.posicaox -= 5
        buracoEstrada.printBuraco(game_display)  
        buracoEstrada2.printBuraco(game_display) 
        buracoEstrada3.printBuraco(game_display)      
        if segundosDesdeUltimoBuraco >= 2:
            sorteio = random.randint(0,1)
            if sorteio == 1:
                sorteioposicao = random.randint(0,11)
                if buracoAtual == 0:
                    buracoEstrada = Buraco(1100,arrayposicao[sorteioposicao])
                    buracoEstrada.printBuraco(game_display)  
                    buracoAtual += 1
                elif buracoAtual == 1:
                    buracoEstrada2 = Buraco(1100,arrayposicao[sorteioposicao]) 
                    buracoEstrada2.printBuraco(game_display)   
                    buracoAtual += 1
                elif buracoAtual == 2:
                    buracoEstrada3 = Buraco(1100,arrayposicao[sorteioposicao])
                    buracoEstrada3.printBuraco(game_display)   
                    buracoAtual = 0   
                             
                            
                segundosDesdeUltimoBuraco = 0    
                #pygame.display.flip()
        car(0, y_carro , game_display , car_running)
        
        
        pygame.display.flip()
        clock.tick(FPS)

#game_loop()

screen = pygame.display.set_mode((1100, 700),0,32)
clock = pygame.time.Clock()
menu = pygame.image.load("Menu.png")
screen.blit(menu,(0,0))
square = pygame.Rect((409,355), (300,61))
square2 = pygame.Rect((409,456), (300,61))
containerBotao1 = pygame.Surface((300,61),pygame.SRCALPHA)
containerBotao2 = pygame.Surface((300,61),pygame.SRCALPHA)


def makeButton(cur):
    if square.collidepoint(cur):
        pygame.display.flip()
        game_loop(screen)
    elif square2.collidepoint(cur):
        print("colocar o ranking")


while True:
   
    screen.blit(containerBotao1, square)
    screen.blit(containerBotao2, square2)
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                makeButton(event.pos)

pygame.display.update()
pygame.event.get()
#pygame.quit()