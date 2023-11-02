from classes import *
from time import sleep

print("Registre-se primeiro: ")
nome = input('Nome: ').strip()
disciplina = input('Disciplina que irá lecionar: ').strip()
professor1 = Professor(nome, disciplina)
sleep(2)
print("Cadastrando...")
sleep(2.5)
print("Tudo pronto\nAgora, você terá um menu de opções:\n")
sleep(1.5)

#Menu opções:
print("[1] - Cadastrar nova disciplina\n[2] - Cadastrar nova atividade\n[3] - Listar atividades pendentes\n[4] - Listar atividades concluídas\n[5] - Marcar atividade como concluída\n[6] - Sair\n")
condicao = False

while not condicao:
  opcao =  int(input("Escolha alguma dessas opções: ").strip())
  print('-'*50)
  while not opcao in [1,2,3,4,5,6]:
    print("Opção inválida. Tente novamente.")
    opcao =  int(input("Escolha alguma dessas opções: "))
    print('-'*50)
  if opcao == 1:
    nome = input('Nome da disciplina: ').strip()
    professor1.adicionar_disciplina(nome)
    print('-'*50)
  elif opcao == 2:
    nome = input('Nome da atividade: ').strip()
    data = input('Data da atividade: ').strip()
    descricao = input('Descrição da atividade: ').strip()
    disciplina = input("Dsiciplina para tal atividade: ").strip()
    professor1.adicionar_atividade(nome, data, descricao, disciplina)
    print('-'*50)
  elif opcao == 3:
    professor1.listar_aberto()
  elif opcao == 4:
    professor1.listar_concluidas()
  elif opcao == 5:
    nome = input('Nome da atividade: ').strip()
    disciplina = input('Nome da disciplina: ').strip()
    professor1.marcar_concluida(nome,disciplina)
    print('-'*50)
  else:
    print("Saindo...")
    print("Até mais!")
    condicao = True
