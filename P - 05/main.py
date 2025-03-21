for i in range(1, 11):   #o Range vai de 1 a 10
    if i % 2 ==0:   #verifica se o número é par (resto da divisão 2 é 0)
        print(f"{i} é par.")
    else:
              print(f"{i} é ímpar")
contador = 1 
while contador <=5: #Continua até contador ser maior que 5
    print(f"contador é {contador}. Estamos no laço While")
    contador += 1 #incrementa 1 no contador a cada repetição
for i in range(1, 11):
    if i == 6:
        print("Número 6 encontrado ! Saindo do laço.")
        break #Sai do laço quando o i for igual a 6
    print(f"Número{i} ainda não é o 6.")
    