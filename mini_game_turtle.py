from turtle import Turtle

#inicializar ma turtle
t = Turtle()

#definir a velocidade
t.speed(1)

while True:

    direcao = input('em qual direção devemos ir? "f:frente" ou "t:trás :"')

    pixel = int(input('Quantos pixels devemos movimentar?'))
    rotacao = input('Rotacionar para d:direita, e: esquerda, n:não rotacionar')
    
    if direcao == 'f' and rotacao == 'n':
        t.forward(pixel)
    elif direcao == 'f' and rotacao == 'd':
        direita = int(input('Quanto para direita devemos rotacionar?'))
        t.right(direita)
        t.forward(pixel)
    elif direcao == 'f' and rotacao == 'e':
        esquerda = int(input('Quanto para esquerda devemos rotacionar?'))
        t.left(esquerda)
        t.forward(pixel)
        
    elif direcao == 't' and rotacao == 'n':
        t.backward(pixel)
    elif direcao == 't' and rotacao == 'd':
        esquerda = int(input('Quanto para direita devemos rotacionar?'))
        t.left(esquerda)
        t.backward(pixel)
    elif direcao == 't' and rotacao == 'e':
        direita = int(input('Quanto para esquerda devemos rotacionar?'))        
        t.right(direita)
        t.backward(pixel) 

    
        
    






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

