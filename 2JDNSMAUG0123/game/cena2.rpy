
label cena2:
    image rua = "image/bg/rua.png"


    show rua
    ia "sei que está triste mas não deixe a vida te abalar! Você ainda tem a oportunidade de desenhar seu próprio destino! A meritocracia americana pe maravilhosa, tanto que você pode escolher as opções a seguir: "

    label escolhamenu:
        menu:
            "CLT":
                jump subescolha_clt
            "terminar estudo":
                jump escola
            "entrar pro crime":
                jump subescolha_crime


    label subescolha_clt:
        menu:

        "Telemarketing":
                # Ação a ser executada quando a opção "Telemarketing" for escolhida

        "Mcdonalds":
                # Ação a ser executada quando a opção "Mcdonalds" for escolhida


    label escola:

        # Ação a ser executada quando a opção "terminar estudo" for escolhida e o personagem voltar triste para casa


    label subescolha_crime:

        menu:
            "Matar":
                # Ação a ser executada quando a opção "Matar" for escolhida

            "Traficar":
                # Ação a ser executada quando a opção "Traficar" for escolhida
=======
label cena2:
   
    show rua
    ia "sei que está triste mas não deixe a vida te abalar! Você ainda tem a oportunidade de desenhar seu próprio destino! A meritocracia americana pe maravilhosa, tanto que você pode escolher as opções a seguir: "

    label escolhamenu:

        if passou_por_subescolha_clt == True and contratado == False:
            menu:
                "Vender Bolo de Pote":
                    jump empreender
                
                "Terminar estudos":
                    jump estudo
                
                "pedir ajuda pros parça":
                    jump subescolha_crime

        elif passou_por_subescolha_clt == True and contratado == True:
            menu:
                "Voltar ao trabalho":
                    jump subescolha_clt

                "Largar o trabalho pra terminar os estudos":
                    jump estudo

                "Ir na onda do mano que ta tirando 5k por dia":
                    jump subescolha_crime

        else:
            menu:
                "Arrumar emprego":
                    jump subescolha_clt

                "terminar estudo":
                    jump estudo

                "entrar pro crime":
                    jump subescolha_crime


label subescolha_clt:
    $ passou_por_subescolha_clt = True
    
    menu:
        "Entrevista":
            # Ação a ser executada quando a opção "Telemarketing" for escolhida
            # entrevista
            scene escritorio

            show principal[2] in left

            narrator "Qual animal você seria na natureza?"
            input 
            narrator "Cite 1 defeito seu"
            input
            narrator "E 1 qualidade?"
            input
            
            $ empregado == renpy.random.choice(["contratado", "nao contratado", "demitido"])

            if empregado == "contratado":
                $ salario = renpy.random.randint(1300, 1600)
                $ contratado = true
                $ tramporandom = renpy.random.choice(["mcdonalds","telemarketing"])
                
                atualizar_mental(10)


                scene escritorio
                narrator f"Parabéns, você foi Contratado para {tramporandom}! Você ganhará um salário de {salario} reais mensais. Volte amanhã para começar."
            
                if tramporandom == "mcdonalds":
                    $ salario = renpy.random.randint(1300, 1600)
                    #aqui faz o codigo dele trampando no mcdonalds

                    if dia == 1:
                        scene mcdonalds
                        show principal[x] in left

                        narrator "É seu primeiro dia, você será o atendente."
                        pause 0.5

                        for i in range(2):

                            if i == 1
                                valor_sanduiche = renpy.random.randint(15, 25)                            

                                # principal aparece na esquerda
                                show principal normal at left

                                #chama qualquer um dos clientes disponiveis
                                show clientemc[renpy.random.randint(0,6)] at right

                                # diálogo
                                principal "Olá seja bem vindo ao mcdonalds"
                                clientemc "Gostaria de um sanduíche big, por favor."
                                principal f"Certo, algo mais? o valor deu R$ {valor_sanduiche}."
                                clientemc "Perfeito, aqui está o dinheiro."
                                clientemc "Obrigada, até mais!"
                                hide clientemc
                                
                            
                            else:
                                valor_sanduiche = renpy.random.randint(15, 25)                            

                                # principal aparece na esquerda
                                show principal normal at left

                                #chama qualquer um dos clientes disponiveis
                                show clientemc[renpy.random.randint(0,6)] at right

                                # diálogo
                                principal "Olá seja bem vindo ao mcdonalds"
                                clientemc "um sanduíche"
                                principal f"Certo, aqlgo mais? Deu R$ {valor_sanduiche}."
                                clientemc "nossa, grosso! não quer trabalhar fica em casa!"
                                principal "entendi foi nada"
                                atualizar_mental(-4)
                                hide clientemc

                        ia "hoje foi tranquilo, como é bom trabalhar! enobrece o homem!"
                        
                        atualizar_fisica(-4)

                        jump volta_pra_casa

                    if dia >= 1 and dia <=4:
                        scene mcdonalds
                        show principal[x] in left

                        narrator f"É seu {i} dia, você sabe o suficiente. Cozinha!"
                        scene black
                        pause 0.5

                        scene cozinhamcdonalds
                        show principal[x] in left

            elif tramporandom == "telemarketing":
                    
                $ salario = renpy.random.randint(1300, 1600)
                #Aqui faz o codigo do telemarketing

                if dia >=5 :
                    scene telemarketing
                    show principal[x] in left

                    narrator "Você será atendente SAC."
                    pause 0.5

                    for i in range(2):

                        if i == 1
                            #tirar dúvida do código com a amanda

                            # principal aparece na direita
                            show principal normal at right

                            #atende sua primeira ligação
                            show clientemultilaser at left

                            # diálogo
                            principal "Central de Relacionamento, PoneiLaser! Bom dia, como posso te ajudar?"
                            clientemultilaser "Olá, então comprei um mouse e ele parou de funcionar"
                            principal "Certo! Vou fazer algumas perguntas padrões, para descobrirmos o que ocorreu e seguir com a melhor forma de garantia. O produto sofreu queda ou teve contato com água?"
                            clientemultilaser "Não, inclusive já fiz os testes do site, e ele continua sem funcionar."
                            principal "Ok, lamento que isto tenha ocorrido com seu mouse, mas pode ficar tranquilo pois seguiremos com a troca expressa, onde seu produto será substituído por um novo!"
                            clientemultilaser "Perfeito, muito obrigado! Tenha um ótimo dia."
                            hide clientemultilaser

                            show principal[x] normal at right
                            chefe "Você precisa trabalhar mais rápido, tem muitos clientes na fila, puxa mais um!"

                            # principal aparece na esquerda
                            show principal normal at left

                            #atende sua terceira ligação do dia
                            show clientemultilaser at right

                            # diálogo
                            principal "Central de Relacionamento, Multilaser! Bom dia, como posso ajudar?"
                            clientemultilaser "Péssimo dia, escuta aqui, comprei o tablet de vocês à 3 meses para dar pra minha filha e a bateria desta porcaria, inchou tanto que está a ponto de explodir, e aí vai fazer o que?"
                            principal f"Ok senhor, pode ficar tranquilo pois..."
                            clientemultilaser "Tranquilo??? Como você me quer tranquilo com uma situação dessas, eu quero meu dinheiro de volta!"
                            principal "Senhor, peço que mantenha a calma pois estou tentando auxiliá-lo."
                            clientemultilaser "Já vi que aqui não vou resolver nada, pode deixar que vou no Procon e no Celso Russomano."
                            principal "Senhor..."
                            clientemultilaser "tu.tu.tu.tu.tu.tu.tu"
                            atualizar_mental(-8)
                            hide clientemultilaserputo

                        ia "Mais um dia maravilhosos concluído! Já posso sentir o cheiro do sucesso emanando de você!"

                        atualizar_fisica(-4)

                        jump volta_pra_casa

                elif dia == 5:
                    scene telemarketing
                    show principal[x] in left

                    narrator "É seu {i} dia, você sabe o suficiente. Agora vai atender telefone e chat!"
                    scene black
                    pause 0.5

                    scene sac
                    show principal[x] in left

                    for i in range(2):
            if i == 1:
                show principal[x] normal at right
                chefe "Você precisa trabalhar mais rápido, tem muitos clientes na fila, puxa mais um!"

                menu:
                    "Trabalhar mais rápido e ficar até mais tarde para ajudar a central a zerar a fila. (+10 em financeiro, -5 em saúde)":
                        # Ação a ser executada quando a opção "Trabalhar mais rápido" for escolhida
                    atualizar_financeiro(10)
                    atualizar_mental(-5)

                    "Recusar a pressão do chefe e manter o ritmo normal. (+5 em saúde)":
                        # Ação a ser executada quando a opção "Manter o ritmo normal" for escolhida
                    atualizar_mental(5)

                hide chefe

            else:
                label volta_pra_casa:
    scene casa
    show principal[3] in left

    narrator "Você volta para casa cansado e desanimado, mesmo tendo feito o seu melhor no trabalho. A situação financeira da sua família continua difícil e sua mãe precisa de tratamento médico."

    principal "É tão injusto... Trabalho tanto, me esforço, mas parece que nunca é o suficiente."

    ia "Não reclame garoto, não vê a sorte que tem de estar trabalhando e ter a oportunidade de realizar seus sonhos? Quem quer vai atrás e não reclama, se você trabalha você consegue viver e investir BASTA QUERER, AGORA VÁ DORMIR PARA TRABALHAR AMANHÃ!"

    # Atualizar variáveis do personagem (exemplo)
    $ saude -= 5
    $ financeiro += 10

    if financeiro >= 0 and saude >= 0 and familia >= 0:
        jump suicidio
    else:
        jump continuar_jogo
>>>>>>> master
