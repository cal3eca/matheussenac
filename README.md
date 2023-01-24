#Estrutura do projeto de Encerramento Do módulo 1 (Fale comigo)

Esse repositório contém os arquivos que foram utilizados para a realização do projeto em grupo, para o encerramento do módulo 1.
No curso de Analise de dados do Senac - Botafogo.
  
Criado por: Diego de Arruda Nieto, Douglas Klem Portugal      
do Amaral, Matheus Barbosa Furtado e Yasmin Belo da Silva                                        
 
Data de criação: 12/01/2023                                   
versão = '3.12'          
  
  
>####PROBLEMA DO PROJETO:
>
>>Sua equipe foi chamada para criar um projeto que vai ajudar com atendimentos automatizados
de dúvidas sobre a empresa e no futuro vai coletar informações para auxiliar na tomada de decisão.
Desenvolvemos um código que lista opções de atendimento e o usuário é guiado por mensagens
avançando dentro desse atendimento simulado até que chegue ao final obtendo a resposta desejada.

>####RESOLUÇÃO:
>
>>Escolhemos uma empresa da área da sáude, no ramo de atuação com coleta labotatorial e clínica diagnóstica.

>>O funcionamento do nosso código, vai de encontro a um sistema de perguntas e respostas prontas
no sentido de que, há mensagens que são enviadas ao usuário de início
onde é perguntado para esse um número de 1 a 5 de sua escolha contendo nesses valores
as funcionalidade da clínica que elx deseja acessar, ou também uma mensagem para sair da aplicação.
Nesse momento são utilizados os comandos (def), para separar as opções que irão estar no chat.

      def questionarioinicio(): # Função criada para chamar as opções iniciais do chat
       print('''Digite uma das opções abaixo:
    1 EXAMES E RESULTADOS
    2 AGENDAMENTOS E CONSULTAS
    3 ORÇAMENTOS
    4 FALAR COM UM DE NOSSOS ATENDENTES
    5 SAIR''')
>
>>Após isso, o programa inicia com um contador no 0
Onde utilizando a função (while) que é um laço de repetição e aqui destacamos que enquanto a váriavel
inicial que está definida em '0', for diferente de um número especifico, o programa continuará executando.

    while inicio != '5': 
    questionarioinicio()
    separador()
    inicio = input('Qual é a opção desejada? ')
    separador()
>
>>Dentro desse laço de repetição, destacamos diversas condições (If, else, elif), onde a partir disso construimos a conversa entre usuário e máquina, através de perguntas e respostas padronizadas.

    if inicio == '1':
        questionario2()
        separador()
        questio2 = input('Qual é a opção desejada para exames? ')
        separador()
        if questio2 == '1':
            print('Clique AQUI para baixar seu exame.')
            questionario3()
            quest3 = input('Qual é a opção desejada? ')
            if quest3 == '1':
                pass 
            elif quest3 == '2':
                print('Saindo...')
                print('Obrigado por escolher a Clínica FAD! Volte sempre!')
                print('#'*100)
                break # O comando break faz com que o atendimento seja encerrado


>
>>ex: Caso usuário escolha no início o número 1, vá para um menu.
existindo aqui, 5 opções de escolha, sendo a última com a função de parar o programa.





#### Funções e Códigos utilizados

> - def > Fazer o conjunto de mensagens que vão aparecer na tela, para a escolha do usuário. 
> 
> - input > Dar o poder de escolha para quem utiliza a aplicação
> 
> - While Criar um laço de repetição onde, acaba a partir de uma instrução específica.
> 
> - If, else, elif > Criar a conversa entre usuário e maquina
> 
> - break > Fazer com que o atendimento seja encerrado
> 
> - pass > Fazer com que o programa faça um looping, e retorne ao início.


