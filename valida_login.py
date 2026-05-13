'''
6 Crie duas variáveis para armazenar um utilizador e uma senha padrão. Peça ao
utilizador para digitar as credenciais e use o operador and para validar o acesso.
'''

usuario = "Davi"
senha = "123"
usuario_digitado = input("Digite usuário: ")
senha_digitada = input("Digite sua senha: ")


if usuario == usuario_digitado and senha == senha_digitada:
    print(f"Acesso liberado, Bem vindo {usuario}")
else:  
    print(f"Usuário ou senha inválidos,tente Novamente")