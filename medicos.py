def novo_medico():
  disponibilidade = True
  while True:
      #CRM
      crm = input("\nDigite o CRM do médico: ")
      if len(crm) == 6:
        if crm in listaMedicos:
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
  listaMedicos[crm] = (nome, crm, especialidade, disponibilidade)
  print("\nMédico cadastrado com sucesso!")

def mostrar_medicos():
  for medico in listaMedicos:
    print(f"Nome: {listaMedicos[medico][0]};\n"
          f"CRM: {listaMedicos[medico][1]};\n"
          f"Especialidade: {listaMedicos[medico][2]};\n"
          f"Dispobilidade: {listaMedicos[medico][3]}.\n")

def deletar_medico():
  """DELETA O MÉDICO DE ACORDO COM O CRM"""
  while True:
    crm = input("\nDigite o CRM do médico que será deletado: ")
    validacao = input(f"Tem certeza que deseja deletar o médico {listaMedicos[crm][0]}?\n"
                      "'S' ou 'N': ").lower()
    if validacao == "s":
      print(f"O médico {listaMedicos[crm][0]} foi deletado com sucesso!")
      listaMedicos.pop(crm)
      break
    elif validacao == "n":
      pass
      break
    else:
      raise ValueError("Opção inválida.")

listaMedicos = {}