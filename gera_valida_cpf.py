def validador_digitos(numero_cpf):
    novo_cpf = numero_cpf[0:9]
    soma = 0
    contador = 9
    digito_verificador = 1

    while contador <= 10:

        for multiplicador, digito in enumerate(novo_cpf[0:contador], -(contador + 1)):
            soma = soma + int(digito) * multiplicador * -1
        print(f'Digito {digito_verificador} = {0 if (soma % 11 < 2) else 11 - (soma % 11)}')

        novo_cpf = novo_cpf + str(0 if (soma % 11 < 2) else 11 - (soma % 11))
        soma = 0
        contador += 1
        digito_verificador += 1
    return novo_cpf

print(f'CPF MANIPULATOR PLUS 0.2b')
while True:
    escolha_menu = input("""O que deseja fazer:
    G - Gerar um CPF
    V - Validar um CPF
    S - Sair\n""")
    if escolha_menu not in 'GgVvSs':
        continue
    elif escolha_menu in 'Gg':
        from random import randint
        cpf = str(randint(100_000_000, 999_999_999))
        print(f'CPF gerado: {validador_digitos(cpf)}\n')
    elif escolha_menu in 'Vv':
        while True:
            cpf = input('Digite o seu cpf (sem símbolos e espaço): ')
            if cpf.isnumeric() and len(cpf) == 11 and len(set(cpf)) > 1:  # Evitar sequencias: ex: 11111111111
                break
            else:
                print('Incorreto!')
        novo_cpf = validador_digitos(cpf)
        confirmando_cpf = 'CPF Correto!' if novo_cpf == cpf else 'CPF INCORRETO!'  # Válido somente para entrada de 11 digitos
        print(novo_cpf, ', ', confirmando_cpf, '\n')  # Mostra o novo CPF
    else:
        break
