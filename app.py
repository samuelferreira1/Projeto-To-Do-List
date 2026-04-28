from utilitarios import adicionar_tarefa, obter_status, continuar_execucao

lista_geral = []
while True:

    nome_da_tarefa = str(input("Nome da Tarefa: "))
    
    status_da_tarefa = obter_status()
    
    adicionar_tarefa(lista_geral, nome_da_tarefa, status_da_tarefa)

    if continuar_execucao() == "N":
        break


print(lista_geral)