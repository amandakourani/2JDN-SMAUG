elif tramporandom == "telemarketing":
    # Código do telemarketing
    if dia == 1:
        scene telemarketing
        show principal[x] in left

        narrator "É seu primeiro dia, você será atendente SAC."
        pause 0.5

        for i in range(2):
            if i == 1:
                # Código para a primeira ligação

                # principal aparece na direita
                show principal normal at right

                # Atende a primeira ligação
                show clientemultilaser[renpy.random.randint(0,6)] at left

                # Diálogo
                principal "Central de Relacionamento, Multilaser! Bom dia, como posso te ajudar?"
                clientemultilaser "Olá, então comprei um mouse e ele parou de funcionar"
                principal "Certo! Vou fazer algumas perguntas padrões, para descobrirmos o que ocorreu e seguir com a melhor forma de garantia. O produto sofreu queda ou teve contato com água?"
                clientemultilaser "Não, inclusive já fiz os testes do site, e ele continua sem funcionar."
                principal "Ok, lamento que isto tenha ocorrido com seu mouse, mas pode ficar tranquilo pois seguiremos com a troca expressa, onde seu produto será substituído por um novo!"
                clientemultilaser "Perfeito, muito obrigado! Tenha um ótimo dia."
                hide clientemultilaser


                # principal aparece na esquerda
                show principal normal at left

                # Atende a terceira ligação do dia
                show clientemultilaserputo[renpy.random.randint(0,6)] at right

                # Diálogo
                principal "Central de Relacionamento, Multilaser! Bom dia, como posso ajudar?"
                clientemultilaserputo "Péssimo dia, escuta aqui, comprei o tablet de vocês há 3 meses para dar para minha filha e a bateria desta porcaria inchou tanto que está a ponto de explodir, e aí, vai fazer o quê?"
                principal f"Ok senhor, pode ficar tranquilo pois..."
                clientemultilaserputo "Tranquilo??? Como vocês querem que eu fique tranquilo com uma situação dessas? Eu quero meu dinheiro de volta!"
                principal "Senhor, peço que mantenha a calma pois estou tentando auxiliá-lo."
                clientemultilaserputo "Já vi que aqui não vou resolver nada, pode deixar que vou no Procon e no Celso Russomano."
                principal "Senhor..."
                telefone "tu.tu.tu.tu.tu.tu.tu"
                atualizar_mental(-8)
                hide clientemultilaserputo

        ia "Mais um dia maravilhoso concluído! Já posso sentir o cheiro do sucesso emanando de você!"

        atualizar_fisica(-4)

        jump volta_pra_casa

    if dia >= 1 and dia <= 4:
        scene telemarketing
        show principal[x] in left

        narrator "É seu {i} dia, você já sabe o suficiente. Agora vai atender telefone e chat!"
        scene black
        pause 0.5

        scene sac
        show principal[x] in left

        # Restante do código para atender ligações e chats

    else:
        # Restante do código para voltar para casa

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

label empreender:
    # Ação a ser executada quando a opção "Vender Bolo de Pote" for escolhida

    scene rua
    show principal[1] in left

    narrator "Você decide empreender e vender bolos de pote."
    pause 0.5

    # Reduz a saúde do p1 devido ao desgaste físico e falta de sono
    atualizar_saude(-10)

    # Aumenta o valor financeiro do p1 devido às vendas
    atualizar_financeiro(15)

    scene empresa
    show principal[1] in left

    narrator "Você vai de porta em porta nas empresas e faculdades, vendendo os bolos de pote."
    pause 0.5

    # Reduz ainda mais a saúde do p1 devido ao esforço físico constante
    atualizar_saude(-5)

    scene rua
    show principal[1] in left

    narrator "Você trabalha duro todos os dias na produção dos bolos e na venda."
    pause 0.5

    scene empresa
    show principal[1] in left

    narrator "Apesar do trabalho árduo, o retorno financeiro não é muito, mas é melhor que nada."
    pause 0.5

    jump volta_pra_casa
