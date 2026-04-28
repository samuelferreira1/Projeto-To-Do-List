from utilitarios import adicionar_tarefa, obter_status, continuar_execucao
from biblioteca_arquivos import json_valido, criar_json, ler_arquivo, salvar_arquivo


ARQUIVO = 'dados.json'

if not json_valido(ARQUIVO):
    criar_json(ARQUIVO)

lista_geral = ler_arquivo(ARQUIVO)

while True:

    nome_da_tarefa = str(input("Nome da Tarefa: "))
    
    status_da_tarefa = obter_status()
    
    adicionar_tarefa(lista_geral, nome_da_tarefa, status_da_tarefa)

    if continuar_execucao() == "N":
        break

salvar_arquivo(ARQUIVO, lista_geral)
print(f"\nDados salvos com sucesso em {ARQUIVO}!")
print(lista_geral)