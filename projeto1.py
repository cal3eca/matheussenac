##################################################################
#  SENAC/RESILIA - Formação em Análise de Dados (FAD)            #
#  Projeto em Grupo - Módulo 1 - Fale Comigo!                    #
#  !/usr/bin/env python3                                         #
#  -*- coding: utf-8 -*-                                         #
#  Criado por: Diego de Arruda Nieto, Douglas Klem Portugal      #
#  do Amaral, Emanoel Cascaes Gomes, Matheus Barbosa Furtado     #
#  e Yasmin Belo da Silva                                        #
#  Data de criação: 12/01/2023                                   #
#  versão = '3.12'                                               #
##################################################################
#
# Atividade:
#
# Sua equipe foi chamada para criar um projeto que vai ajudar com atendimentos automatizados
# de dúvidas sobre a empresa e no futuro vai coletar informações para auxiliar na tomada de decisão.
# Desenvolvemos um código que lista opções de atendimento e o usuário é guiado por mensagens
# avançando dentro desse atendimento simulado até que chegue ao final obtendo a resposta desejada.
#
# Escolhemos uma empresa no ramo de atuação com coleta labotatorial e clínica diagnóstica, como
# mostrado a seguir:
#
print('#'*100)
print('Bem-vindo ao chatbot da Clínica FAD! Aqui você encontra informações rápidas sobre nossos serviços.')
print('#'*100)


def questionarioinicio(): # Função criada para chamar as opções iniciais do chat
    print('''Digite uma das opções abaixo:
1 EXAMES E RESULTADOS
2 AGENDAMENTOS E CONSULTAS
3 ORÇAMENTOS
4 FALAR COM UM DE NOSSOS ATENDENTES
5 SAIR''')


def questionario2():# função criada para printar as opções sobre exames e resultados
    print('''
1 BAIXAR EXAME
2 IMPRIMIR EXAME
3 ENCAMINHAR EXAME PARA SEU MÉDICO
4 EXCLUIR EXAME''')


def questionario3(): #Função criada para printar as opções de saída ou de retorno às opções iniciais
    print('''
1 VOLTAR AO INÍCIO
2 SAIR''')


def quesconsultas1():# Função criada para printar as opções sobre agendamentos e consultas
    print('''
1 VER CONSULTAS AGENDADAS
2 CANCELAR UMA CONSULTA
3 REMARCAR UMA CONSULTA''')


def quesconsultas2():#Função criada para printar as oploes sobre orçamentos
    print('''
1 CONSULTAR PREÇOS DISPONÍVEIS
2 ADICIONAR UM ORÇAMENTO SIMULADO
3 REMOVER UM ORÇAMENTO SIMULADO''')


def quesconsultas3(): #Função criada para printar as opções de contato
    print('''
1 TELEFONES  
2 REDES SOCIAIS
3 ENCAMINHAMENTO INTERNO''')





def separador():
    print('*'*30)


inicio = '' #Esta variável foi criada para dar início ao chatbot e receber as entradas relacionadas às opções

while inicio != '5': # Enquanto a váriavel inicio for difernete de 5, o programa continua em execução, caso seja inserido o valor 5 o chat é finalizado
    questionarioinicio()# chamando as opções iniciais
    separador()# separando com *
    inicio = input('Qual é a opção desejada? ')# atribuindo um valor(opção) à variável início
    separador()
    if inicio == '1':# Entrando na condicional, se o valor atribuído à variável início for 1 a função para referente a opção 1 é chamada
        questionario2()# Função referente à opção 1(Exames)
        separador()
        questio2 = input('Qual é a opção desejada para exames? ')# A variável questio2 foi criada para receber as entradas referente às opções sobre exames
        separador()
        if questio2 == '1':# caso a variável questio2 receba o valor 1, referente as opções da função quistionario2, o usuário será levado à página de downloads de exames
            print('Clique AQUI para baixar seu exame.')
            questionario3()# opções de sair ou reiniciar atendimento
            quest3 = input('Qual é a opção desejada? ')#variável criada para para trabalhar com a condicional de sair ou retornar ao inicio, na linha abaixo
            if quest3 == '1':
                pass # o comando pass faz com que o atendimento retorne ao início
            elif quest3 == '2':
                print('Saindo...')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break # O comando break faz com que o atendimento seja encerrado
        if questio2 == '2':# se questio2 receber o valor 2 referente a imprimir exame, abrirá para o usuáiro a opção de imprimir exames
            print('Clique AQUI para imprimir seu exame.')

            questionario3() # chamando as opções de sair ou finalizar atendimento, explicado nas linhas 93 - 101
            quest3 = input('Qual é a opção desejada?')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
            separador()
        if questio2 == '3':# Se o questio2 receber o valor 3 a opção de encaminhar exame será apresentada
            print('Clique AQUI para encaminhar seu exame.')

            questionario3()# questionário de saída ou reinício de atendimento, explicado nas linhas 93 - 101
            quest3 = input('Qual é a opção desejada?')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
            separador()
        if questio2 == '4': # Se questio2 receber 4, será apresentada a opção de excluir exame
            print('Clique AQUI para excluir seu exame.')

            questionario3()# opções de saída ou reinício, explicado nas linhas 93 - 101
            quest3 = input('Qual é a opção desejada?')
            if quest3 == '1':
                pass
            elif quest3 == '2': # Variável que receberá a opção de saír
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
            separador()
    elif inicio == '2':# entrando na condicional da opção 2 (Agendamentos e consultas)
        quesconsultas1()
        separador()
        questio1 = input('Qual é a opção desejada?') # variável que vai receber a opção desejada sobre agendamentos e consultas
        separador()# separando com *
        if questio1 == '1':# entrando na condicional opção 1 (ver consultas agendadas)
            print('Clique AQUI para ver suas consultas agendadas.')
            questionario3()
            quest3 = input('Qual é a opção desejada?')#variável que vai receber as opções de finalização ou retorno ao início
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print("Saindo.")
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break

        elif questio1 == '2':# entrando na condicional opção 2 (cancelamento de consulta)
            print('Clique AQUI para cancelar sua consulta.')
            questionario3()
            quest3 = input('Qual é a opção desejada?')# variável que vai receber as opções de saida ou retorno ao início
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
        elif questio1 == '3':# Entando na condicional opção 3(remarcar consulta)
            print('Clique AQUI para remarcar uma consulta previamente agendada.')
            questionario3()
            quest3 = input('Qual é a opção desejada?')#variável que vai receber as opções de saída ou retorno ao início
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
    elif inicio == '3': # entrando na condicional opção 3 do questionário inicial (orçamentos)
        quesconsultas2() #Questionário de orçamentos
        separador()
        questio1 = input('Qual é a opção desejada?')#variável que vai receber a opção desejada sobre orçamentos
        separador()
        if questio1 == '1': # Entrando na condicional opção 1 sobre orçamentos  ver (preços)
            print(
                'Clique AQUI para ver os preços de acordo com a tabela de exames atual.')
            questionario3()# questionário de saída ou retorno ao início
            quest3 = input('Qual é a opção desejada?') # variável que vai receber as opções de saída ou retorno ao início
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print("Saindo.")
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break

        elif questio1 == '2': # Entrando na condicional opção 2 sobre orçamentos (simulação de orçamento)
            print('Clique AQUI para adicionar uma simulação de orçamento.')
            questionario3()
            quest3 = input('Qual é a opção desejada?') # variável que vai receber as opções de saída ou retorno ao início
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
        elif questio1 == '3': # Entrando na condicional opçao 3 de orçamentos( remover simulação de orçamento)
            print('Clique AQUI para remover uma simulação de orçamento.')
            questionario3()
            quest3 = input('Qual é a opção desejada?')# variável que vai receber as opções de saída ou retorno ao início
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
    elif inicio == '4':# Entrando na condicional do questionário inicial opção 4: falar com um atendente
        quesconsultas3() # Questionário da opção 4
        separador()
        questio1 = input('Qual é a opção desejada?') #Variável que vai receber a opçao refernte à falar com um atendente
        separador()
        if questio1 == '1': # Entrando na condicional opção 1 (telefones disponíveis) dentro de falar com um atendente
            print(
                'Clique AQUI para acessar os telefones disponíveis.')
            questionario3() # questionário de saída ou retorno ao início
            quest3 = input('Qual é a opção desejada?') # variável que vai receber as opções de saída ou retorno ao início
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print("Saindo.")
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break

        elif questio1 == '2':# Entrando na condicional opção 2 (redes sociais) dentro de falar com um atendente
            print('Clique AQUI para acessar nossas redes sociais.')
            questionario3() # questionário de saída ou retorno ao início
            quest3 = input('Qual é a opção desejada?')# variável que vai receber as opções de saída ou retorno ao início
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
        elif questio1 == '3':# Entrando na condicional opção 3 (outros meios de comunicações) dentro de falar com um atendente
            print('Não encontrou meios de nos contactar? Deixe uma mensagem com suas informações que retornaremos o mais breve possível:')
            questionario3()# questionário de saída ou retorno ao início
            quest3 = input('Qual é a opção desejada?') # variável que vai receber as opções de saída ou retorno ao início
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo.')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break
else:
    print('Obrigado por escolher a Clínica FAD! Volte sempre!')
    print('#'*100)
#
# Referências (último acesso em 15/01/2023):
# https://sergiofranco.com.br/
# https://www.dremerson.com.br/


