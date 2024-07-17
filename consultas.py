import medicos
import pacientes

id_consulta = 0
lista_consultas = {}

def nova_consulta():
    """Agenda uma nova consulta."""
    global id_consulta
    # Obtém a lista de médicos e pacientes
    lista_medicos = medicos.lista_medicos
    lista_pacientes = pacientes.lista_pacientes

    # Solicita o cpf do paciente
    cpf = input("Para qual paciente a consulta será agendada: Informe o CPF: ").lower()

    # Verifica se o cpf é válido
    if len(cpf) != 11:
        print("Formato de CPF inválido. Tente novamente.")
        return
    
    # Verifica se o paciente está cadastrado
    if cpf not in lista_pacientes:
        print("Paciente não cadastrado.")
        return
    
    # Solicita o CRM do médico
    crm = input(f"Com qual médico você deseja cadastrar a consulta de {lista_pacientes[cpf][0]}? Informe o CRM: ").lower()
    
    # Verifica se o CRM é válido
    if len(crm) != 6:
        print("Formato de CRM inválido. Tente novamente.")
        return

    # Verifica se o médico está cadastrado
    if crm not in lista_medicos:
        print("Médico não cadastrado. Tente novamente.")
        return

    # Obtém a disponibilidade do médico
    disponibilidade = lista_medicos[crm][3]

    # Verifica a disponibilidade do médico
    if not disponibilidade:
        print("Médico indisponível para consultas.")
        return

    # Agenda a consulta
    try:
        print(f"Consulta de {lista_pacientes[cpf][0]} com {lista_medicos[crm][0]} foi marcada com sucesso!\n")
        lista_medicos[crm][3] = False
        id_consulta += 1
        lista_consultas[id_consulta] = (lista_medicos[crm], lista_pacientes[cpf])
    except Exception as e:
        print(f"Erro ao agendar consulta: {e}")

def mostrar_consultas():
    """Mostra as consultas cadastradas"""
    global id_consulta
    lista_medicos = medicos.lista_medicos

    # Recebe o CRM do médico
    crm = input("Qual médico você deseja verificar as consultas? Informe o CRM: ").lower()

    if len(crm) != 6:
        print("Formato de CRM inválido. Tente novamente.")
        return

    # Verifica se há consultas cadastradas para o médico informado
    if crm not in lista_medicos:
        print("CRM não cadastrado. Tente novamente.")
        return
    
    consultas_agendadas = [f"{consulta[1][0]} com {consulta[0][0]}" for consulta in lista_consultas.values() if consulta[0][1] == crm]
    
    if consultas_agendadas:
        print(f"{lista_medicos[crm][0]} possui as seguintes consultas agendadas: ")
        for consulta in consultas_agendadas:
            print(consulta)