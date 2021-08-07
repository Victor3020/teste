import turtle
import random

xbola = round(random.uniform(0.01, 0.5), 2)
ybola = round(random.uniform(0.01, 0.5), 2)

#tela de fundo
altura = 1280
largura = 720
tela = turtle.Screen()
tela.bgcolor("black")
tela.title("Pongada")
tela.tracer(0)
tela.setup(width=altura, height=largura)

#Placar
placar = turtle.Turtle()
placar.speed(0)
placar.color("orange")
placar.penup()
placar.hideturtle
placar.goto(0,280)
placar.write("Jogador 1: 0  Jogador 2: 0", align="center", font=("Sams",24,"normal"))

#Pontuação
score_1=0
score_2=0

# barra esquerda
barra_Esq=turtle.Turtle()
barra_Esq.penup()
barra_Esq.shape('square')
barra_Esq.shapesize(stretch_wid=5, stretch_len=1)
barra_Esq.speed(0)
barra_Esq.goto(-(largura/2)-50,0)
barra_Esq.color('purple')


# barra direita
barra_Dir=turtle.Turtle()
barra_Dir.penup()
barra_Dir.shape('square')
barra_Dir.shapesize(stretch_wid=5, stretch_len=1)
barra_Dir.speed(0)
barra_Dir.goto((largura/2)+50,0)
barra_Dir.color('purple')

#bola
bola=turtle.Turtle()
bola.penup()
bola.shape('circle')
bola.speed(0)
bola.goto(0,0)
bola.color('white')
bola.dx= xbola
bola.dy= ybola


#Andar para cima
def barra_Esq_Cima():
    y = barra_Esq.ycor()
     
    if y <= 270:
        y += 30
        barra_Esq.sety(y)

#Andar para baixo        
def barra_Esq_Baixo():
    y = barra_Esq.ycor() 
    barra_Esq.sety(y)
    
    if y >= -270:
        y -= 30
        barra_Esq.sety(y)

#Andar para Cima
def barra_Dir_Cima():
    y = barra_Dir.ycor()
     
    if y <= 270:
        y += 30
        barra_Dir.sety(y)

#Andar para Baixo        
def barra_Dir_Baixo():
    y = barra_Dir.ycor() 
    barra_Dir.sety(y)
    
    if y >= -270:
        y -= 30
        barra_Dir.sety(y)

#Função para mexer no teclado
tela.listen()
tela.onkeypress(barra_Esq_Cima, "w")
tela.onkeypress(barra_Esq_Baixo,"s")
tela.onkeypress(barra_Dir_Cima, "Up")
tela.onkeypress(barra_Dir_Baixo,"Down")

while True:
    tela.update() 
    #bola movendo
    bola.sety(bola.ycor()+bola.dy)
    bola.setx(bola.xcor()+bola.dx)
    #bola batendo
    if bola.ycor()>290:
        bola.sety(290)
        bola.dy *=-1
    if bola.ycor()<-290:
        bola.sety(-290)
        bola.dy *=-1
    if bola.xcor()>410:
        bola.goto(0,0)
        score_1 +=1
        placar.clear()
        placar.write("Jogador 1: {}  Jogador 2: {}".format(score_1,score_2), align="center", font=("Sams",24,"normal"))
        aleatorio = round(random.randrange(2))
        if aleatorio == 0:
            bola.dx = round(random.uniform(0.09, 0.5), 2)
        elif aleatorio == 1:
            bola.dx = round(random.uniform(-0.09, -0.5), 2)
        bola.dx *=-1

    if bola.xcor()<-410:
        bola.goto(0,0)
        score_2+=1
        placar.clear()
        placar.write("Jogador 1: {}  Jogador 2: {}".format(score_1,score_2), align="center", font=("Sams",24,"normal"))
        aleatorio = round(random.randrange(2))
        if aleatorio == 0:
            bola.dx = round(random.uniform(0.09, 0.5), 2)
        elif aleatorio == 1:
            bola.dx = round(random.uniform(-0.09, -0.5), 2)
        bola.dx *=-1
    # colisão da bola com as barras
    if (bola.xcor() > 380 and bola.xcor() < 390) and (bola.ycor() < barra_Dir.ycor()+50 and bola.ycor() > barra_Dir.ycor()-50):
        bola.dx *=-1
    if (bola.xcor() < -380 and bola.xcor() > -390) and (bola.ycor() < barra_Esq.ycor()+50 and bola.ycor() > barra_Esq.ycor()-50):
        bola.dx *=-1
