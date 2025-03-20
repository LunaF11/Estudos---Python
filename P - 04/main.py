#Criando a lista de frutas
minha_lista_de_frutas = ["Maçã", "Banana", "Laranja"]

#imprimindo a lista
print(minha_lista_de_frutas)

#adicionando um item a lista
minha_lista_de_frutas.append("Uva") # Aqui adicionamos mais uma fruta para a nossa lista !
print(minha_lista_de_frutas) #Colocando ".append" a fruta "abacaxi" será adicionado na lista.

#Acessando um item da lista
print(minha_lista_de_frutas[0]) #Vai imprimir "maçã" porque está na posição 0
print(minha_lista_de_frutas[1]) #Vai imprimir "Banana" porque está na posição 1

#Modificando um item da lista
minha_lista_de_frutas[1] ="Abacaxi" #Troca "banana" por "Abacaxi"
print(minha_lista_de_frutas) #Logo depois dessa modificação, "Abacaxi" ira ir para a posição [1]

minha_lista_de_frutas.remove("Laranja") #Utilizando ".remove" para remover um item da lista
print(minha_lista_de_frutas) #Agora a ordem da lista estará: Maçã, Abacaxi e uva