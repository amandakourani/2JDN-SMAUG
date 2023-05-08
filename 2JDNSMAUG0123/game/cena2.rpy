label cena2:
   
    show rua
    ia "sei que está triste mas não deixe a vida te abalar! Você ainda tem a oportunidade de desenhar seu próprio destino! A meritocracia americana pe maravilhosa, tanto que você pode escolher as opções a seguir: "

    label escolhamenu:

        if passou_por_subescolha_clt == True and contratado == False:
            menu:
                "Vender Bolo de Pote"
                    jump empreender
                
                "Terminar estudos"
                    jump estudo
                
                "pedir ajuda pros parça"
                    jump subescolha_crime

        elif passou_por_subescolha_clt == True and contratado == True:
            menu:
                "Voltar ao trabalho"
                    jump subescolha_clt

                "Largar o trabalho pra terminar os estudos"
                    jump estudo

                "Ir na onda do mano que ta tirando 5k por dia"
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
    passou_por_subescolha_clt = True
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

                            if i ==1
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

                        narrator "É seu {i} dia, você sabe o suficiente. Cozinha!"
                        scene black
                        pause 0.5

                        scene cozinhamcdonalds
                        show principal[x] in left


                elif tramporandom == "telemarketing":
                    #$ salario = renpy.random.randint(1300, 1600)
                    #Aqui faz o codigo do telemarketing

            else:
                #escrever cena dele voltando pra casa triste embora tenha feito o seu melhor
                jump volta_pra_casa
                        
        "Vender Bolo de Pote":
            jump empreender

label empreender:
    #script da venda de bolo de pote


label estudo:
    # Ação a ser executada quando a opção "terminar estudo" for escolhida


label subescolha_crime:

    if passou_por_subescolha_clt == True:
        jump demissao
        
    menu:
        "Roubar":
            # Ação a ser executada quando a opção "Roubar" for escolhida

        "Traficar":
            # Ação a ser executada quando a opção "Traficar" for escolhida


  