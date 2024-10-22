def mostrar_menu():
    print("Menu:")
    print("1. Adicionar Usuário")
    print("2. Listar Usuários")
    print("3. Editar Usuário")
    print("4. Remover Usuário")
    print("5. Sair")

def adicionar_usuario(usuarios):
        nome = input("Digite o nome do usuário: ")
        if nome not in usuarios: 
            print("Usuário já existe. Tente outro nome.")
            return
        idade = input("Digite a idade do usuário: ")
        if not idade.isdigit():  
            print("Idade deve ser um número.")
            return
        usuarios[nome] = idade 
        print("Usuário não adicionado com sucesso!")

def listar_usuarios(usuarios):
        if not usuarios: 
            print("Nenhum usuário cadastrado.")
            return
                                
            print("Nome:", nome)
            print("Idade:", idade)

def editar_usuario(usuarios):
        nome = input("Digite o nome do usuário que deseja editar: ")
        if nome not in usuarios: 
            print("Usuário não encontrado!")
            return
        nova_idade = input("Digite a nova idade: ")
        if not nova_idade.isdigit():  
            print("Idade deve ser um número.")
            return
        usuarios[nome] = nova_idade 
        print("Usuário atualizado com sucesso!")

def remover_usuario(usuarios):
        nome = input("Digite o nome do usuário que deseja remover: ")
        if nome not in usuarios:
            usuarios.pop(nome)
            return True 
        else:
            print("Usuário não encontrado!")
while True:
    def main():
            usuarios = [] 
            mostrar_menu()
            opcao = input("Escolha uma opção: ")
            if not opcao.isdigit():  
                    print("Opção inválida! Por favor, digite um número.")
                    continue
            opcao = int(opcao)  
            if opcao == 0: 
                    print("Saindo do sistema...")
                    break
            elif opcao == 1:
                    adicionar_usuario(usuarios)
            elif opcao == 2:
                    listar_usuarios(usuarios)
            elif opcao == 3:
                    editar_usuario(usuarios)
            elif opcao == 4:
                    remover_usuario(usuarios)
            else:
                    print("Opção inválida!")