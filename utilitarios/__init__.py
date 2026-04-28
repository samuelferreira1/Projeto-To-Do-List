def adicionar_tarefa(lista_tarefas:list, nome:str, status:str) -> None:
    nova_tarefa = {
        "nome_da_tarefa":nome, 
        "status_da_tarefa":status
    }
    lista_tarefas.append(nova_tarefa)

def obter_status() -> str: 
    while True:
        status_da_tarefa = str(input("Status da Tarefa [Pendente / Concluído]: ")).capitalize().strip()
        if status_da_tarefa in ["Pendente", "Concluído"]:
            return status_da_tarefa
        print(f"A opção \"{status_da_tarefa}\" não existe! Por favor, digite exatamete [Pendente / Concluído]")

def continuar_execucao() -> str:
     while True:
        opcao = str(input("Deseja continuar? [S/N] ")).upper()
        if opcao in ["S", "N"]:
            return opcao
        print(f"A opção \"{opcao}\" não existe! Por favor, digite exatamete [S/N] ")



