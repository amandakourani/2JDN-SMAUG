label empreender:
    # Ação a ser executada quando a opção "Vender Bolo de Pote" for escolhida
    
    scene rua
    show principal[1] in left
    
    narrator "Você decide empreender e vender bolos de pote."
    pause 0.5
    
    # Reduz a saúde do principal devido ao desgaste físico e falta de sono
    atualizar_saude(-10)
    
    # Aumenta o valor financeiro do principal devido às vendas
    atualizar_financeiro(15)
    
    scene rua
    show principal[1] in left
    
    narrator "Você vai de porta em porta nas empresas e faculdades, vendendo os bolos de pote."
    pause 0.5
    
    # Reduz ainda mais a saúde do principal devido ao esforço físico constante
    atualizar_saude(-5)
    
    scene casa
    show principal[1] in left
    
    narrator "Você trabalha duro todos os dias na produção dos bolos e na venda."

    ia "Isso mesmo, produza bastante, lembre-se que com apenas 1 real você consegue construir um império!"

    pause 0.5
    
    scene rua
    show principal[1] in left
    
    principal "Estou quebrado, trabalhando muito e recebendo pouco. Mas bora, vou seguir, é melhor que nada."
    pause 0.5
    
    scene rua
    show principal[1] in left
    
    menu:
        "Continuar trabalhando na rua":
            # Ação a ser executada quando a opção "Continuar trabalhando na barraca" for escolhida
            
            scene rua noite
            show principal[1] in left
            
            ia "Continue trabalhando, o descanso não vai te trazer dinheiro, a única coisa que te traz dinheiro é o seu esforço!"

            principal "Cara, eu estou moído, mas vou ficar até a saída do pessoal da noite, com certeza mais alguém vai comprar meus bolos."

            pause 0.5
            
            # Reduz ainda mais a saúde do principal devido ao esforço físico constante
            atualizar_saude(-10)
            
            jump volta_pra_casa
        
        "Fechar a barraca e descansar um pouco":
            # Ação a ser executada quando a opção "Fechar a barraca e descansar um pouco" for escolhida
            
            scene rua tarde
            show principal[1] in left
            
            ia "NÃO ACREDITO QUE VOCÊ ESTÁ INDO EMBORA! TRABALHE ENQUANTO ELES DORMEM, TRABALHE ENQUANTO ELES DORMEM, TRABALHE ENQUANTO ELES DORMEM."

            principal "Estou muito cansado, não consigo andar mais nem uma quadra, vou para casa descansar, amanhã tem mais."
            pause 0.5
            
            # Aumenta a saúde do principal devido ao descanso
            atualizar_saude(5)
            
            jump volta_pra_casa


   label terminar_estudos:
    # Ação a ser executada quando a opção "Terminar os estudos" for escolhida

    scene faculdade
    show principal[1] in left

    narrator "Você decide terminar os estudos e se dedicar ao seu crescimento acadêmico."
    pause 0.5

    # Reduz a saúde mental do p1 devido à preocupação com a saúde da mãe
    atualizar_saude_mental(-15)

    scene casa
    show principal[1] in left

    narrator "Enquanto você se dedica aos estudos, a saúde da sua mãe continua piorando."
    pause 0.5

    # Reduz ainda mais a saúde mental do p1 devido à preocupação contínua
    atualizar_saude_mental(-10)

    scene hospital
    show principal[1] in left

    narrator "Você visita sua mãe no hospital e se sente impotente por não poder ajudá-la financeiramente."
    pause 0.5

    jump volta_pra_casa