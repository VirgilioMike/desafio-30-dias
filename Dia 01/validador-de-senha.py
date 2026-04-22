#VAriavel para receber a senha do usuário
senha = input('Digite a senha: ')

#Validar se a senha tem o mínimo de 8 caracteres
if len(senha) >= 8:
    print("Tamanho OK")
else:
    print("Senha muito curta NOK")

#Validar se tem pelo menos 1 letra maiúscula
if any(c.isupper() for c in senha):
    print("Tem maiúscula OK")
else:
    print("Falta maiúscula NOK")

#Validar se tem pelo menos 1 letra minúscula
if any(c.islower() for c in senha):
    print("Tem minúscula OK")
else:
    print("Falta minúscula NOK")

#Validar se tem pelo menos 1 número
if any(c.isdigit() for c in senha):
    print("Tem número OK")
else:
    print("Falta número NOK")

#Validar se tem pelo menos 1 caractere especial
especiais = "!@#$%^&*"
if any(c in especiais for c in senha):
    print("Tem caractere especial OK")
else:
    print("Falta caractere especial NOK")