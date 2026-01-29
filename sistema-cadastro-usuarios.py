def exibir_menu():
  print("\n--- Sistema de Cadastro de Usuários ---\n")
  print("1 - Cadastrar usuário:")
  print("2 - Listar usuário:")
  print("3 - Buscar usuário por nome:")
  print("4 - Remover usuário:")
  print("0 - Sair")

def cadastrar_usuario(usuarios):
  print("\n--- Cadastro de Usuário: ---\n")

  while True:
    nome = input("Digite o seu nome: ").strip()
    if nome:
      break
    else:
      print("Erro: o nome não pode ser vazio.")
  
  while True:
    try:
      idade = int(input("Digite a sua idade: "))
      if idade > 0:
        break
      else:
        print("Erro: digite um número positivo.")     
    except ValueError:
      print("Erro: digite um número válido para a idade.")

  while True:
    email = input("Digite o seu e-mail: ").strip()
    if "@" in email and "." in email:
      break
    else:
      print("Erro: e-mail inválido. Tente novamente.")

  usuarios.append({
    "nome": nome,
    "idade": idade,
    "e-mail": email,
  })
  print("\nUsuário cadastrado com êxito!")

def listar_usuarios(usuarios):
  print("\n--- Lista de Usuários: ---")

  if not usuarios:
    print("Nenhum usuário cadastrado!")
    return
  
  for indice, usuario in enumerate(usuarios, start=1):
    print(f"{indice}. Nome: {usuario["nome"]} | Idade: {usuario["idade"]} | E-mail: {usuario["e-mail"]}")
  
def main():
  usuarios = []

  while True:
    exibir_menu()

    try:
      opcao = int(input("\nEscolha a opção desejada: "))
    except ValueError:
      print("Erro: entrada inválida. Digite um número válido.")
      continue
    
    if opcao == 1:
      cadastrar_usuario(usuarios)
    elif opcao == 2:
      listar_usuarios(usuarios)
    elif opcao == 3:
      print("Buscar usuário por nome:")
    elif opcao == 4:
      print("Remover usuário:")
    elif opcao == 0:
      print("Encerrando o sistema...")
      break
    else:
      print("Erro: opção inexistente.")

if __name__ == '__main__':
  main()