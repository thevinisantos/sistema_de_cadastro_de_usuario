def exibir_menu():
  print("\n--- Sistema de Cadastro de Usuários ---")
  print("1 - Cadastrar usuário:")
  print("2 - Listar usuário:")
  print("3 - Buscar usuário por nome:")
  print("4 - Remover usuário:")
  print("0 - Sair")

def cadastrar_usuario(usuarios):
  print("\n--- Cadastro de Usuário: ---")

  while True:
    nome = input("Digite o seu nome: ").strip()
    if nome:
      break
    else:
      print("O nome não pode ser vazio.")
  
  while True:
    try:
      idade = int(input("Digite a sua idade: "))
      if idade > 0:
        break
      else:
        print("Digite um número positivo.")     
    except ValueError:
      print("Digite um número válido para a idade.")

  while True:
    email = input("Digite o seu e-mail: ").strip()
    if "@" in email and "." in email:
      break
    else:
      print("E-mail inválido. Tente novamente.")

  usuarios.append({
    "nome": nome,
    "idade": idade,
    "e-mail": email,
  })
  print("Usuário cadastrado com êxito!")

def main():
  usuarios = []

  while True:
    exibir_menu()

    try:
      opcao = int(input("Escolha a opção desejada: "))
    except ValueError:
      print("Entrada inválida. Digite um número válido.")
      continue
    
    if opcao == 1:
      cadastrar_usuario(usuarios)
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