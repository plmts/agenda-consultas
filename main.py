import pacientes
import medicos
import consultas

def funcao_paciente():
  while True:
    print("O que você deseja?\n")
    resposta = int(input("1 - Verificar pacientes cadastrados;\n"
          "2 - Cadastrar novo paciente;\n"
          "3 - Deletar paciente cadastrado;\n"
          "4 - Voltar ao menu anterior;\n"
          "Resposta: "))
    try:
      if resposta in range(1,5):
        if resposta == 1:
          pacientes.mostrar_pacientes()
        elif resposta == 2:
          pacientes.novo_paciente()
        elif resposta == 3:
          pacientes.deletar_paciente()
        elif resposta == 4:
          programa()
          break
      else:
        pass
    except:
      print("\nFavor, utilizar as opções disponíveis")

def funcao_medico():
  while True:
    print("O que você deseja?\n")
    resposta = int(input("1 - Verificar médicos cadastrados;\n"
          "2 - Cadastrar novo médico;\n"
          "3 - Deletar médico cadastrado;\n"
          "4 - Voltar ao menu anterior;\n"
          "Resposta: "))
    try:
      if resposta in range(1,5):
        if resposta == 1:
          medicos.mostrar_medicos()
        elif resposta == 2:
          medicos.novo_medico()
        elif resposta == 3:
          medicos.deletar_medico()
        elif resposta == 4:
          programa()
          break
      else:
        print("\nFavor, utilizar as opções disponíveis")
    except:
      break

def funcao_consultas():
  while True:
    print("O que você deseja?\n")
    resposta = int(input("1 - Verificar consultas agendadas;\n"
          "2 - Cadastrar nova consulta;\n"
          "3 - Deletar consulta cadastrada;\n"
          "4 - Voltar ao menu anterior;\n"
          "Resposta: "))
    try:
      if resposta in range(1,5):
        if resposta == 1:
          consultas.mostrar_consultas()
        elif resposta == 2:
          consultas.nova_consulta()
        elif resposta == 3:
          print("deletar consulta")
        elif resposta == 4:
          programa()
          break
      else:
        pass
    except:
      print("\nFavor, utilizar as opções disponíveis")

def programa():
    while True:
      try:
        print("Seja bem vindo ao agendador de consultas. O que você deseja verificar? ")
        question = int(input("1 - Pacientes;\n"
              "2 - Consultas;\n"
              "3 - Médicos;\n"
              "4 - Sair.\n"
              "Resposta: "))
        if question in range(1,5):
          if question == 1:
            funcao_paciente()
          elif question == 2:
            funcao_consultas()
          elif question == 3:
            funcao_medico()
          elif question == 4:
            print("\nObrigado. Até a próxima.")
            break
        else:
          print("\nPor favor, utilize as opções disponíveis.\n")
          programa()
      except:
        print("\nOps, algo deu errado. Tente novamente.\n")
        programa()
      else:
        break

programa()