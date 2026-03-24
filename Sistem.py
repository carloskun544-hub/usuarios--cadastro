import json

arquivo = "usuarios.json"
def carregar():
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def salvar(usuarios):
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f, indent=2)

def ver_all(usuario):
    for u in usuario:
        print(f'nome: {u["nome"]} | id: {u["id"]} ')

def gerar_id(usuarios):
    if not usuarios:
        return 1
    return max(u["id"] for u in usuarios) + 1
def add_usuario(usuario):
    
    nome_novo = input("Nome: ")
    for n in usuario:
        if nome_novo.lower() == n["nome"].lower():
            print("Esse nome já foi cadastrado")
            return 
            
    id = gerar_id(usuario)
    adici = {
        "nome": nome_novo,
        "id": id
    }
    usuario.append(adici)
    salvar(usuario)
    print("Adicionado com sucesso!")

def alterar(usuario):
    id_al = int(input("digite o id do user: "))

    usuario_encontrado = None


    for u in usuario:
        if id_al == u["id"]:
            usuario_encontrado = u
            break

    if usuario_encontrado is None:
        
        print("id não encontrado")
        return

    nome_n = input("novo nome: ")

    for u in usuario:
        if nome_n == u["nome"] and u["id"] != id_al:
            print("esse nome já está cadastrado")
            return


    usuario_encontrado["nome"] = nome_n
    salvar(usuario)
    print("alterado com sucesso!")
        
    
   
        


def remover(usuario):
    remo = input("nome: ")
    id_remo = int(input("id: "))
    for u in usuario:
        if remo == u["nome"]:
            if id_remo == u["id"]:
                usuario.remove(u)
                salvar(usuario)
                print("removido com sucesso!")
                return
    
    print("usuario não encontrado")


usuarios = carregar()

while True:
    print("1 - adicionar ")
    print("2 - ver todos os usuarios")
    print("3 - remover usuario")
    print("4 - alterar usuarios")
    e = input("digite sua escolha: ")
    if e == "1":
        add_usuario(usuarios)
    elif e == "2":
        ver_all(usuarios)
    elif e == "3":
        remover(usuarios)
    elif e == "4":
        alterar(usuarios)

    