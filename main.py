from pacientes import Paciente

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
          Paciente.mostrar_pacientes()
        elif resposta == 2:
          Paciente.novo_paciente()
        elif resposta == 3:
          Paciente.deletar_paciente()
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
              "3 - Sair\n"
              "Resposta: "))
        if question in range(1,4):
          if question == 1:
            funcao_paciente()
          elif question == 2:
            print("consultas")
          elif question == 3:
            print("\nObrigado. Até a próxima.")
            break
        else:
          print("\nerro 1;")
          programa()
          break
      except:
        print("\nerro 2;")
        programa()
        break
      else:
        break

programa()