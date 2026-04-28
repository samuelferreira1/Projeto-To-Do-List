import json

def json_valido(nome):
    try:
        with open(nome, 'r', encoding='utf-8') as f:
            json.load(f)
        return True
    except (FileNotFoundError, json.JSONDecodeError):
        return False

def criar_json(nome):
    try:
        with open(nome, 'w', encoding='utf-8') as a:
            json.dump([], a)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    else:
        print(f"O arquivo {nome} foi criado e está pronto para uso!")

def ler_arquivo(nome):
    try:
        with open(nome, 'r', encoding='utf-8') as a:
            return json.load(a)
    except Exception as e:
        print(f"Ocorreu um erro inesperado {e}")
        return []
    
def salvar_arquivo(nome, lista):
    try:
        with open (nome, 'w', encoding='utf-8') as a:
            json.dump(lista, a, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")