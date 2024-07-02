import medicos
import pacientes



def nova_consulta():
  listaMedicos = medicos.listaMedicos
  while True:
    crm = input("Com qual médico você deseja se consultar: informe o CRM: ").lower()
    if crm in listaMedicos[crm]:
      if listaMedicos[crm][3] == False:
        print("Médico indisponível para consultas.")
      elif listaMedicos[crm][3] == True:
        medicos.marcar_consulta(crm)
        break
      else:
        print("Algo deu errado. Tente novamente!")
        break
    elif crm not in listaMedicos:
      print("CRM não cadastrado.")
      break
    else:
      print("CRM inválido. Tente novamente")

