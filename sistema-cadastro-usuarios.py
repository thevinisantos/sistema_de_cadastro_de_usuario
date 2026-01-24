def exibir_menu():
  print("\n--- Sistema de Cadastro de Usuários ---")
  print("1 - Cadastrar usuário:")
  print("2 - Listar usuário:")
  print("3 - Buscar usuário por nome:")
  print("4 - Remover usuário:")
  print("0 - Sair")

def main():
  usuarios = []

  while True:
    exibir_menu()

    try:
      opcao = int(input("Escolha a opção desejada: "))
    except ValueError:
      print("Entrada inválida. Digite um número.")
      break
    
    if opcao == 1:
      print("Cadastrar usuário")
    elif opcao == 2:
      print("Listar usuários:")
    elif opcao == 3:
      print("Buscar usuário por nome:")
    elif opcao == 4:
      print("Remover usuário:")
    elif opcao == 0:
      print("Encerrando o sistema...")
      break
    else:
      print("Opção inexistente.")

if __name__ == '__main__':
  main()