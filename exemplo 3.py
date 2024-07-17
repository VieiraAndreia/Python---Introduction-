#cálculo do salário líquido de um professor - teste 3 do diagrama de blocos
#vh é valor da hora aula
#nh é número de horas trabalhadas
#vb é valor bruto do salário
#sl é salário líquido

vh=int(input("Digite o valor da hora aula:"))
nh=int(input("Digite o número de horas trabalhadas:"))
inss= int(input("Digite o valor do percentual de desconto do INSS:"))
vb=vh+nh
sl=vb-inss/100
print(sl)