from config import SessionLocal, engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
#TABELA
class Paciente(Base):
  __tablename__ = "Pacientes"
  id = Column(Integer, primary_key=True, autoincrement=True)
  cpf = Column(String(11), unique=True, nullable=False)
  nome = Column(String(50), nullable=False)
  contato = Column(String(11), nullable=False)


Base.metadata.create_all(bind=engine)

def novo_paciente():
    """ADICIONA NOVO PACIENTE AO BANCO DE DADOS USANDO O CPF COMO CHAVE PRINCIPAL"""
    # Inicializa a sessão
    session = SessionLocal()

    # Verifica se o CPF é válido
    cpf = input("\nDigite o CPF do paciente: ")
    if len(cpf) != 11:
        print("Formato de CPF inválido. Tente novamente.")
        return

    # Verifica se o paciente já está cadastrado
    paciente_existente = session.query(Paciente).filter(Paciente.cpf == cpf).first()
    if paciente_existente:
        print("Paciente já cadastrado.")
        session.close()
        return

    # Nome
    nome = input("\nDigite o nome completo do paciente: ")
    if not isinstance(nome, str) or nome.strip() == "":
        print("\nNome inválido!")
        session.close()
        return

    # Contato
    contato = input("\nDigite a forma para contato com o paciente: ")
    if contato.strip() == "":
        print("\nForma de contato inválida. Tente novamente!")
        session.close()
        return

    # Adiciona ao banco de dados
    novo_paciente = Paciente(cpf=cpf, nome=nome, contato=contato)
    session.add(novo_paciente)
    session.commit()
    session.close()
    print("\nPaciente cadastrado com sucesso!")

def deletar_paciente():
    """DELETA O PACIENTE DE ACORDO COM O CPF"""
    # Inicializa a sessão
    session = SessionLocal()

    cpf = input("\nDigite o CPF do paciente que será deletado: ")
    paciente = session.query(Paciente).filter(Paciente.cpf == cpf).first()
    if paciente:
        validacao = input(f"Tem certeza que deseja deletar o paciente {paciente.nome}?\n"
                          "'S' ou 'N': ").lower()
        if validacao == "s":
            session.delete(paciente)
            session.commit()
            print(f"Paciente {paciente.nome} deletado com sucesso!")
        elif validacao == "n":
            pass
        else:
            raise ValueError("Opção inválida.")
    else:
        print("Paciente não encontrado.")

    session.close()

def mostrar_pacientes():
    """MOSTRA TODOS OS PACIENTES CADASTRADOS"""
    # Inicializa a sessão
    session = SessionLocal()

    pacientes = session.query(Paciente).all()
    if not pacientes:
        print("Não há pacientes cadastrados.")
    else:
        for paciente in pacientes:
            print(f"Nome: {paciente.nome};\n"
                  f"CPF: {paciente.cpf};\n"
                  f"Contato: {paciente.contato};\n")

    session.close()



novo_paciente()


# def novo_paciente():
#   """ADICIONA NOVO PACIENTE AO DICIONÁRIO DE PACIENTES USANDO O CPF COMO CHAVE PRINCIPAL"""
#   # Verifica se o cpf é válido
#   cpf = input("\nDigite o cpf do paciente: ")
#   if len(cpf) != 11:
#     print("Formato de CPF inválido. Tente novamente.")
#     return

#   if cpf in lista_pacientes:
#     print("Paciente já cadastrado.")
#     return

#   #NOME
#   nome = input("\nDigite o nome completo do paciente: ")
#   if not isinstance(nome, str) or nome == "" or nome.strip() == "":
#     print("\nNome inválio!")

    
#   #CONTATO
#   contato = input("\nDigite a forma para contato com o paciente: ")
#   if contato == "" or contato.strip() == "":
#     print("\nForma de contato inválida. Tente novamente!")

#   #ADICIONA AO DICIONÁRIO
#   lista_pacientes[cpf] = (nome, cpf, contato)
#   print("\nPaciente cadastrado com sucesso!")
#   return cpf

# def deletar_paciente():
#   """DELETA O PACIENTE DE ACORDO COM O CPF"""
#   cpf = input("\nDigite o CPF do paciente que será deletado: ")
#   validacao = input(f"Tem certeza que deseja deletar o paciente {lista_pacientes[cpf][0]}?\n"
#                     "'S' ou 'N': ").lower()
#   if validacao == "s":
#     print(f"Paciente {lista_pacientes[cpf][0]} deletado com sucesso!")
#     lista_pacientes.pop(cpf)
#   elif validacao == "n":
#     pass
#   else:
#     raise ValueError("Opção inválida.")

# def mostrar_pacientes():
#   if not lista_pacientes:
#     print("Não há pacientes cadastrados.")
#     return
  
#   for paciente in lista_pacientes:
#     print(f"Nome: {lista_pacientes[paciente][0]};\n"
#           f"CPF: {lista_pacientes[paciente][1]};\n"
#           f"Contato: {lista_pacientes[paciente][2]};\n")
    
# lista_pacientes = { '12345678910': ['paulo matos', '12345678910', 'email'],
#                    '12345678911': ['tony stark', '12345678911', 'telefone']  }