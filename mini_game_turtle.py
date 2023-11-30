from turtle import Turtle

t = Turtle()
t.speed(1)

def lados():

    if movimentar_para_lado == 'd':
            angulo = int(input('Quanto para direita devemos rotacionar?'))
            t.right(angulo)
    elif movimentar_para_lado == 'e':
            angulo = int(input('Quanto para esquerda devemos rotacionar?'))
            t.left(angulo)
    t.forward(distancia)
    

while True:
    
    direcao = input('Para qual direção devemos ir? "f:frente" ou "t:trás :"') 

    if direcao == 'f':
        distancia = int(input('Quantos pixels devemos movimentar para frente?'))
        movimentar_para_lado = input('Rotacionar para d:direita, e: esquerda, n:não rotacionar')
        lados()

    else:
        direcao == 't'
        distancia = int(input('Quantos pixels devemos movimentar para trás?'))
        movimentar_para_lado = input('Rotacionar para d:direita, e: esquerda, n:não rotacionar')
        lados() 

    resposta = input('Continuar andando?')
    if resposta not in ('sim', 's'):
        break
        
    






# #Movimentar a turtle para frente
# t.forward(100)

# #rotacionar em x graus para direita
# t.right(90)
# t.forward(100)

# #rotacionar em x graus para esquerda
# t.left(90)
# t.forward(100)

# #movimentar a turtle para trás
# t.backward(200)
# input()

