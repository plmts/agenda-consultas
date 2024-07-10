import medicos
import pacientes



def nova_consulta():
    """Agenda uma nova consulta."""

    # Obtém a lista de médicos
    lista_medicos = medicos.listaMedicos

    # Solicita o CRM do médico
    crm = input("Com qual médico você deseja se consultar? Informe o CRM: ").lower()

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
    if disponibilidade == False:
        print("Médico indisponível para consultas.")
        return

    # Agenda a consulta
    try:
        medicos.marcar_consulta(crm)
    except:
        pass
