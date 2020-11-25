import pygame
import random
import contextvars

pygame.init()
window_width = 1100
window_height = 700
arrayvelocidade = [10,20,25,50]
arrayposicao = [115,130,140,270,315,415,240,420,400]
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


def game_loop(game_display , NomePlayer):
    print("player que ta jogando é : " + NomePlayer)
    pontosFps = 0
    pontos = 0
    level = 0
    fonte = pygame.font.Font(None , 30)
    
    
    posicaoCarro = 0
    fundo = pygame.Surface((1100,700))
    fundo.fill(pygame.Color(0,100,10))
    pygame.display.set_caption("Running Over Holes")

    gameOver = pygame.image.load("gameover.png")
    gameOver = pygame.transform.scale(gameOver, (1100 , 700))

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
        nivel = fonte.render(("Nivel: " + str(level)) , (0,0) ,(255,255,255))
        pontosFps += 1
        if pontosFps % 60 == 0:
            pontos +=100
            segundosDesdeUltimoBuraco += 1
        fundo.blit(placar,(0,35))
        fundo.blit(nivel,(200,35))          
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
                
        if pontos == 500:
            level = 1
        elif pontos == 2000:
            level = 2 
        elif pontos == 4000:
            level = 3      
        game_display.blit(fundo,(0,0))
        posicaoEstrada -= arrayvelocidade[level]
        if posicaoEstrada <= -1099:
            posicaoEstrada = 1099
        game_display.blit(estrada,(posicaoEstrada,100))
        posicaoEstrada2 -= arrayvelocidade[level]
        if posicaoEstrada2 <= -1099:
            posicaoEstrada2 = 1099
        game_display.blit(estrada,(posicaoEstrada2,100))
        
        game_display.blit(superficieDivisoria,(0,100))
        game_display.blit(superficieDivisoria,(0,100))
        game_display.blit(superficieDivisoriaBaixo,(0,585))
        game_display.blit(superficieDivisoriaBaixo,(0,585))

        buracoEstrada.posicaox -= arrayvelocidade[level]
        buracoEstrada2.posicaox -= arrayvelocidade[level]
        buracoEstrada3.posicaox -= arrayvelocidade[level]
        buracoEstrada.printBuraco(game_display)  
        buracoEstrada2.printBuraco(game_display) 
        buracoEstrada3.printBuraco(game_display)      
        if segundosDesdeUltimoBuraco >= 1/(level+1):
            sorteio = random.randint(0,1)
            if sorteio == 1:
                sorteioposicao = random.randint(0,8)
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
        if posicaoCarro == 0:
            if (buracoEstrada.posicaox == 0 and (buracoEstrada.posicaoy + 130/2) >= 115 and (buracoEstrada.posicaoy + 130/2) <= 230 ) or (buracoEstrada2.posicaox == 0 and (buracoEstrada2.posicaoy + 130/2) >= 115 and (buracoEstrada2.posicaoy + 130/2) <= 230 ) or (buracoEstrada3.posicaox == 0 and (buracoEstrada3.posicaoy + 130/2) >= 115 and (buracoEstrada3.posicaoy + 130/2) <= 230 ):
                running = False 
        elif posicaoCarro == 1:
            if (buracoEstrada.posicaox == 0 and (buracoEstrada.posicaoy + 130/2) >= 287 and (buracoEstrada.posicaoy + 130/2) <= 402 ) or (buracoEstrada2.posicaox == 0 and (buracoEstrada2.posicaoy + 130/2) >= 287 and (buracoEstrada2.posicaoy + 130/2) <= 402 ) or (buracoEstrada3.posicaox == 0 and (buracoEstrada3.posicaoy + 130/2) >= 287 and (buracoEstrada3.posicaoy + 130/2) <= 402 ):
                running = False 
        elif posicaoCarro == 2: 
            if (buracoEstrada.posicaox == 0 and (buracoEstrada.posicaoy + 130/2) >= 459 and (buracoEstrada.posicaoy + 130/2) <= 574 ) or (buracoEstrada2.posicaox == 0 and (buracoEstrada2.posicaoy + 130/2) >= 459 and (buracoEstrada2.posicaoy + 130/2) <= 574 ) or (buracoEstrada3.posicaox == 0 and (buracoEstrada3.posicaoy + 130/2) >= 459 and (buracoEstrada3.posicaoy + 130/2) <= 574 ):
                running = False 
        pygame.display.flip()
        clock.tick(FPS)
    game_display.blit(gameOver,(0,0)) 
    fonte = pygame.font.Font(None , 90)
    placar = fonte.render(("Sua pontuação final foi de: " + str(pontos)) , (0,0) ,(255,255,255))
    fonte = pygame.font.Font(None , 40)
    MensagemMenu = fonte.render("Pressione ESC para voltar para o menu principal", (0,0) ,(255,255,255)) 
    game_display.blit(placar,(70,300)) 
    game_display.blit(MensagemMenu,(70,500)) 
    arquivo = open("Ranking.txt", "a")
    arquivo.writelines("-> " + NomePlayer + ":" + str(pontos) + "\n")
    arquivo.close()
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:               
                if event.key == pygame.K_ESCAPE:
                    menuTela(screen)  
#game_loop()
def nomePlayer(screen):
    fonte = pygame.font.Font(None , 30)
    screen.fill((0,0,0))
    NomePlayer = ""
    Nome = fonte.render("",(0,0) ,(255,255,255))
    PerguntaNome = fonte.render("Digite seu Nome: ", (0,0) ,(255,255,255))
    screen.blit(PerguntaNome,(70,300))
    pygame.display.flip()
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False
                    game_loop(screen, NomePlayer)
                elif event.key == pygame.K_BACKSPACE:
                    NomePlayer = NomePlayer[:-1]
                    screen.fill((0,0,0))
                    screen.blit(PerguntaNome,(70,300))
                    Nome = fonte.render(NomePlayer,(0,0) ,(255,255,255))
                    screen.blit(Nome,(250,300))
                    pygame.display.flip()    
                else:
                    NomePlayer += event.unicode
                    screen.fill((0,0,0))
                    screen.blit(PerguntaNome,(70,300))
                    Nome = fonte.render(NomePlayer,(0,0) ,(255,255,255))
                    screen.blit(Nome,(250,300))
                    pygame.display.flip()
screen = pygame.display.set_mode((1100, 700),0,32)
clock = pygame.time.Clock()
menu = pygame.image.load("Menu.png")
screen.blit(menu,(0,0))
square = pygame.Rect((409,355), (300,61))
square2 = pygame.Rect((409,456), (300,61))
containerBotao1 = pygame.Surface((300,61),pygame.SRCALPHA)
containerBotao2 = pygame.Surface((300,61),pygame.SRCALPHA)

class ItemPlacar:
    def __init__(self,nome, pontos):
        self.nome = nome
        self.pontos = pontos
       

    

def ranking(screen):
    arrayOrdena = []
    y = 50
    fonte = pygame.font.Font(None , 50)
    screen.fill((0,0,0))
    rankingLabel = fonte.render("Ranking : ", 0,(255,255,255))
    screen.blit(rankingLabel,(420,10))
    pygame.display.flip()
    arquivo = open("Ranking.txt","a+")
    leitura = [x.strip() for x in arquivo]
    if len(leitura) > 0:
        for player in leitura:
            nomeSplit = player.split(":")
            arrayOrdena.append(ItemPlacar(nomeSplit[0], nomeSplit[1]))
        
        print(arrayOrdena) 
        arrayOrdena.sort(key=lambda x: x.pontos, reverse=True)   
        for item in arrayOrdena:     
            label = fonte.render(item.nome + ":" + item.pontos,0,(255,255,255))  
            screen.blit(label,(420,y))
            y += 40 
        pygame.display.flip()

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                print("xavasca")
                if event.key == pygame.K_ESCAPE:
                    menuTela(screen)
                    
def makeButton(cur):
    if square.collidepoint(cur):
        pygame.display.flip()
        #game_loop(screen)
        nomePlayer(screen)
    elif square2.collidepoint(cur):
        ranking(screen)


def menuTela(screen):
    screen = pygame.display.set_mode((1100, 700),0,32)
    clock = pygame.time.Clock()
    menu = pygame.image.load("Menu.png")
    screen.blit(menu,(0,0))
    square = pygame.Rect((409,355), (300,61))
    square2 = pygame.Rect((409,456), (300,61))
    containerBotao1 = pygame.Surface((300,61),pygame.SRCALPHA)
    containerBotao2 = pygame.Surface((300,61),pygame.SRCALPHA)
    pygame.display.flip()
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
menuTela(screen)    
#pygame.quit()