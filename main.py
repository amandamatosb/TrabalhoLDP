import os
import time

def mudanca():
  os.system('clear')
  print(lista)
  print('\nvocê deseja fazer alguma mudança?')
  r = input('digite "s" para sim e "n" para não: ')
  if r == 'n':
    os.system('clear')
    print('\ntudo certo, inserção de alunos e notas finalizado com sucesso\n')
    print('//NOTAS//')
    print(lista) 
    
  else:
    alterar_excluir()

def alterar_excluir():
  os.system('clear')
  print(lista)
  print('\n1. alterar nota \n2. excluir aluno')
  r1 = int(input('qual função você deseja realizar? '))
  
  nome1 = input('digite o nome de quem você deseja realizar a mudança: ')


  if r1 == 1 and nome1 in lista.keys():
    nota_nova = float(input('digite a nota nova: '))
    lista[nome1] = nota_nova
    mudanca()
      
  elif r1 == 2 and nome1 in lista.keys():
    lista.pop(nome1)
    mudanca()

  else:
    print('\n*aluno inexistente*')
    time.sleep(3)
    mudanca()
 
lista = {}

i=1
x = int(input('quantos alunos você tem? '))

while i<=x:
  nome = input('digite o nome do aluno: ')
  if lista.get(nome):
    print('esse nome já existe, use outro nome.')
    print('\n')
  else:
    nota = float(input('digite a nota do aluno: '))
    lista[nome] = nota
    i = i+1
    print('\n')

mudanca()