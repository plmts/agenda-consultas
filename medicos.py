import consultas

def novo_medico():
  disponibilidade = True
  while True:
      #CRM
      crm = input("\nDigite o CRM do médico: ")
      if len(crm) == 6:
        if crm in lista_medicos:
          raise print("CRM já cadastrado")
        break
      else:
        print("\nCRM inválido, tente novamente!")

  while True:
      #NOME
      nome = input("\nDigite o nome completo do médico: ")
      if not isinstance(nome, str) or nome == "" or nome.strip() == "":
        print("\nNome inválio!")
      else:
        break
      
  while True:
      #especialidade
      especialidade = input("\nDigite a especilidade do médico: ")
      if especialidade == "" or especialidade.strip() == "":
        print("\nEspecialiade inválida. Tente novamente!")
      else:
        break
    #ADICIONA AO DICIONÁRIO
  lista_medicos[crm] = (nome, crm, especialidade, disponibilidade)
  print("\nMédico cadastrado com sucesso!")

def mostrar_medicos():
  if not lista_medicos:
    print("Não há médicos cadastrados. Tente novamente!")
    return

  for medico in lista_medicos:
    print(f"Nome: {lista_medicos[medico][0]};\n"
          f"CRM: {lista_medicos[medico][1]};\n"
          f"Especialidade: {lista_medicos[medico][2]};\n"
          f"Dispobilidade: {lista_medicos[medico][3]}.\n")

def deletar_medico():
  """DELETA O MÉDICO DE ACORDO COM O CRM"""
  while True:
    crm = input("\nDigite o CRM do médico que será deletado: ")
    validacao = input(f"Tem certeza que deseja deletar o médico {lista_medicos[crm][0]}?\n"
                      "'S' ou 'N': ").lower()
    if validacao == "s":
      print(f"O médico {lista_medicos[crm][0]} foi deletado com sucesso!\n")
      lista_medicos.pop(crm)
      break
    elif validacao == "n":
      pass
      break
    else:
      raise ValueError("Opção inválida.")

def marcar_consulta():
  consultas.nova_consulta()


lista_medicos = { '123456' : ['joao jose', '123456', 'blares', True]}