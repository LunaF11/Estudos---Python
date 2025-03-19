idade = int( input("Informe sua idade: "))

if idade >= 18:
    print("Você está permitido a entrar !")
else:
    print("Você não está permitido a entrar !")
    
salario = float( input("Informe seu salário:"))

if salario <= 3000:
    print("Programador junior")
elif salario > 3000 and salario <= 6000:
    print("Programador plenor")
elif salario > 6000 and salario <= 15000:
    print("Programador senior")
else:
    print("Gerente de Projetos")
