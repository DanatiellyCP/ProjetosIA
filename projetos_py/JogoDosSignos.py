#Esse algoritmo serve para descobrir o signo de uma pessoa
#fornecendo o dia e o mês de nacsimento.

mesEntrada = input("Digite o mês que você nasceu: ")
mes = int(mesEntrada)

diaEntrada = input("Digite o dia que você nasceu: ")
dia = int(diaEntrada)

if (((mes == 1) and (dia >= 20)) or ((mes == 2) and (dia <= 18))):
	print ("Você é do signo de Aquario")

if (((mes == 2) and (dia >= 19)) or ((mes == 3) and (dia <= 20))):
	print("Você é do signo de Peixes")

if (((mes == 3) and (dia >= 21)) or ((mes == 4) and (dia <= 19))):
	print("Você é do signo de Aries")

if (((mes == 4) and (dia >= 20)) or ((mes == 5) and (dia <= 20))):
	print("Você é do signo de touro")

if (((mes == 5) and (dia >= 21)) or ((mes == 6) and (dia <= 20))):
	print("Você é do signo de Gemeos")

if (((mes == 6) and (dia >= 21)) or ((mes == 7) and (dia <= 22))):
	print("Você é do signo de Cancer")

if (((mes == 7) and (dia >= 23)) or ((mes == 8) and (dia <= 22))):
	print("Você é do signo de Leão")

if (((mes == 8) and (dia >= 23)) or ((mes == 9) and (dia <= 22))):
	print("Você é do signo de Virgem")

if (((mes == 9) and (dia >= 23)) or ((mes == 10) and (dia <= 22))):
	print("Você é do signo de Libra")

if (((mes == 10) and (dia >= 23)) or ((mes == 11) and (dia <= 21))):
	print("Você é do signo de Escorpião")

if (((mes == 11) and (dia >= 22)) or ((mes == 12) and (dia <= 21))):
	print("Você é do signo de Sargitário")

if (((mes == 12) and (dia >= 22)) or ((mes == 1) and (dia <= 19))):
	print("Você é do signo de Capricórnio")
