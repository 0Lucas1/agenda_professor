class Atividade:

  def __init__(self, nome, data, descricao,disciplina):
    self.nome = nome
    self.data = data
    self.descricao = descricao
    self.disciplina = disciplina
    self.concluida = False

class Disciplina:
  def __init__(self,nome):
    self.nome = nome
    self.lista_atividade = []



class Professor:
  def __init__(self, nome, disciplina):
    self.nome = nome
    self.lista_concluidas = []
    self.lista_nao_concluidas = []
    self.lista_disciplinas = []
    self.lista_disciplinas.append(Disciplina(disciplina))
  
  def adicionar_disciplina(self,disciplina):
      for disciplina_interavel in self.lista_disciplinas:
        if disciplina_interavel.nome == disciplina:
          print(f"A disciplina {disciplina} já está cadastrada.")
          return None
      self.lista_disciplinas.append(Disciplina(disciplina))
        
          
  def adicionar_atividade(self,nome,data,descricao,disciplina):
      for disciplina_interavel in self.lista_disciplinas:
        if disciplina_interavel.nome == disciplina:
          for atividade_interavel in disciplina_interavel.lista_atividade:
            if atividade_interavel.nome == nome:
              print("Erro: atividade já existe.")
              return None
            elif atividade_interavel.data == data:
              print("Erro: datas iguais na mesma disciplina.")
              return None
            else:
              pass
          atividade = Atividade(nome,data,descricao,disciplina)
          self.lista_nao_concluidas.append(atividade)
          disciplina_interavel.lista_atividade.append(atividade)
          return None
        else:
          pass
          
      else:
        print("Erro: disciplina não existe.")
        

    
  def marcar_concluida(self,nome, disciplina):
    if not len(self.lista_nao_concluidas) and not len(self.lista_concluidas):
      print("Você ainda não cadastrou nenhuma atividade.")
    else:
      for disciplina_interavel in self.lista_disciplinas:
        if disciplina_interavel.nome == disciplina:
          for atividade_interavel in disciplina_interavel.lista_atividade:
            if atividade_interavel.nome == nome:
              if atividade_interavel.concluida:
                print("Erro: atividade já foi concluída.")
                return None
              else:
                atividade_interavel.concluida = True
                self.lista_concluidas.append(atividade_interavel)
                self.lista_nao_concluidas.remove(atividade_interavel)
                print("Atividade marcada como concluída.")
                return None
          else:
            print('Atividade não encontrada.')
            return None
        else:
          pass
      else:
        print("Dicisplina não existe.")
      
  def listar_concluidas(self):
    if  not len(self.lista_nao_concluidas) and not len(self.lista_concluidas):
      print('Você ainda não adicionou nenhuma atividade.')
      print('-'*50)
    elif not len(self.lista_concluidas):
      print("Você ainda não tem atividades concluídas.")
      print('-'*50)
    else:
      for pos, atividade_concluida in enumerate(self.lista_concluidas):
        print(f'Posição na lista: {pos}')
        print(f'Nome: {atividade_concluida.nome}')
        print(f'Data: {atividade_concluida.data}')
        print(f'Descrição: {atividade_concluida.descricao}')
        print(f'Disciplina: {atividade_concluida.disciplina}')
        print(f'Concluída: {atividade_concluida.concluida}')
        print('-'*50)
  def listar_aberto(self):
    if not  len(self.lista_nao_concluidas) and not len(self.lista_concluidas):
      print('Você ainda não adicionou nenhuma atividade.')
      print('-'*50)
    elif not len(self.lista_nao_concluidas):
      print('Você não tem atividades pendentes.')
      print('-'*50)
    else:
      
      for pos, atividade_aberta in enumerate(self.lista_nao_concluidas):
        print(f'Posição na lista: {pos}')
        print(f'Nome: {atividade_aberta.nome}')
        print(f'Data: {atividade_aberta.data}')
        print(f'Descrição: {atividade_aberta.descricao}')
        print(f'Disciplina: {atividade_aberta.disciplina}')
        print(f'Concluída: {atividade_aberta.concluida}')
        print('-'*50)
      