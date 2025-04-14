  '''
     1)   confirmação de senha
'''
                senha1 = input('Digite a sua senha')
        senha2 = input('Repita sua senha')
        if senha1 == senha2:
          print('Acesso permitido')
        else:
          print('Senha não coincidiram')
'''

    2)    pedir dois números ao usuário e exibir o maior e se forem iguais
'''
        n1 = int(input("Digite um numero"))
        n2 = int(input("Digite um numero"))
        if n1 > n2:
          print(f'o numero {n1} é maior que o numero {n2}')
        elif n1<n2:
          print(f'o número {n2} é maior que o numero {n1}')
        else:
           print('os numeros são iguais')


'''
       3) informar a média do aluno
 '''      
        n1 = float(input("Digiet sua nota"))
        n2 = float(input("Digiet sua nota"))
        n3 = float(input("Digiet sua nota"))
        m = n1 + n2 + n3
        mf = m / 3
        if mf >= 7:
          print('Aprovado')
        else:
            print('Reprovado')




'''
        4)informar se a letra digitada é uma vogal ou consoante
''''
        letra = str(input('Digite uma letra'))
        if letra == 'a' and 'e' and 'i' and 'o' and 'u':
         print(f'a letra {letra} é uma vogal')
         else:
           print(f'a letra {letra} é uma consoante')



'''
                5)colocar os numeros digitados pelo usuario em ordem decrescente
'''
        n1 = int(input("Digite o primeito numero"))
        n2 = int(input("Digite o segundo numero"))
        n3 = int(input("Digite o  terceiro numero"))
        listadenumeros = [n1, n2, n3]
          print(f' "a lista em ordem invertida é : " {sorted(listadenumeros, reverse=trure)}')


'''
        6) quantidade de litros usados em uma viagem
'''
        tempo= float(input("informe o tempo gasto:"))
        velocidade= float(input("informe a velocidade media: "))
        distancia= tempo * velocidade
        litros = distancia / 12
        print("a quantidade de ml usados é:", litros)


    