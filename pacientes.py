class Paciente():
  pacientes = {}
  def novo_paciente():
    """ADICIONA NOVO PACIENTE AO DICIONÁRIO DE PACIENTES USANDO O CPF COMO CHAVE PRINCIPAL"""
    while True:
      #CPF
      cpf = input("\nDigite o cpf do paciente: ")
      if len(cpf) == 11:
        if cpf in Paciente.pacientes:
          raise print("CPF já cadastrado")
        break
      else:
        print("\nCPF inválido, tente novamente!")

    while True:
      #NOME
      nome = input("\nDigite o nome completo do paciente: ")
      if not isinstance(nome, str) or nome == "" or nome.strip() == "":
        print("\nNome inválio!")
      else:
        break
      
    while True:
      #CONTATO
      contato = input("\nDigite a forma para contato com o paciente: ")
      if contato == "" or contato.strip() == "":
        print("\nForma de contato inválida. Tente novamente!")
      else:
        break
    #ADICIONA AO DICIONÁRIO
    Paciente.pacientes[cpf] = (nome, cpf, contato)
    print("\nPaciente cadastrado com sucesso!")
    return cpf
  
  def deletar_paciente():
    """DELETA O PACIENTE DE ACORDO COM O CPF"""
    while True:
      cpf = input("\nDigite o CPF do paciente que será deletado: ")
      validacao = input(f"Tem certeza que deseja deletar o paciente {Paciente.pacientes[cpf][0]}?\n"
                        "'S' ou 'N': ").lower()
      if validacao == "s":
        print(f"Paciente {Paciente.pacientes[cpf][0]} deletado com sucesso!")
        Paciente.pacientes.pop(cpf)
        break
      elif validacao == "n":
        pass
        break
      else:
        raise ValueError("Opção inválida.")


  def mostrar_pacientes():
    for paciente in Paciente.pacientes:
      print(f"Nome: {Paciente.pacientes[paciente][0]};\n"
            f"CPF: {Paciente.pacientes[paciente][1]};\n"
            f"Contato: {Paciente.pacientes[paciente][2]};\n")