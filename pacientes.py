def novo_paciente():
  """ADICIONA NOVO PACIENTE AO DICIONÁRIO DE PACIENTES USANDO O CPF COMO CHAVE PRINCIPAL"""
  # Verifica se o cpf é válio
  cpf = input("\nDigite o cpf do paciente: ")
  if len(cpf) != 11:
    print("Formato de CPF inválido. Tente novamente.")
    return

  if cpf in lista_pacientes:
    print("Paciente já cadastrado.")
    return

  #NOME
  nome = input("\nDigite o nome completo do paciente: ")
  if not isinstance(nome, str) or nome == "" or nome.strip() == "":
    print("\nNome inválio!")

    
  #CONTATO
  contato = input("\nDigite a forma para contato com o paciente: ")
  if contato == "" or contato.strip() == "":
    print("\nForma de contato inválida. Tente novamente!")

  #ADICIONA AO DICIONÁRIO
  lista_pacientes[cpf] = (nome, cpf, contato)
  print("\nPaciente cadastrado com sucesso!")
  return cpf

def deletar_paciente():
  """DELETA O PACIENTE DE ACORDO COM O CPF"""
  cpf = input("\nDigite o CPF do paciente que será deletado: ")
  validacao = input(f"Tem certeza que deseja deletar o paciente {lista_pacientes[cpf][0]}?\n"
                    "'S' ou 'N': ").lower()
  if validacao == "s":
    print(f"Paciente {lista_pacientes[cpf][0]} deletado com sucesso!")
    lista_pacientes.pop(cpf)
  elif validacao == "n":
    pass
  else:
    raise ValueError("Opção inválida.")

def mostrar_pacientes():
  if not lista_pacientes:
    print("Não há pacientes cadastrados.")
    return
  
  for paciente in lista_pacientes:
    print(f"Nome: {lista_pacientes[paciente][0]};\n"
          f"CPF: {lista_pacientes[paciente][1]};\n"
          f"Contato: {lista_pacientes[paciente][2]};\n")
    
lista_pacientes = { '12345678910': ['paulo matos', '12345678910', 'email'],
                   '12345678911': ['tony stark', '12345678911', 'telefone']  }