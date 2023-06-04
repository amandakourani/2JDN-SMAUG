label dilema_financeiro:

    scene mesa_contas
    show principal[1] in left
    
    narrador "As contas estão chegando e você precisa decidir o que pagar primeiro."
    
    menu:
        "Pagar o aluguel antes que seja tarde demais":
            atualizar_financeiro(-20)
            $ financeiro += -20,
            atualizar_mental(-10)
            $ mental += -10,
        
        "Pagar a conta de luz para evitar cortes":
            atualizar_financeiro(-10)
            $ financeiro += -10,
            atualizar_mental(-5)
            $ mental += -5,
    
    menu:
        "Pedir um empréstimo com juros altos":
            atualizar_financeiro(-30)
            $ financeiro += -30,
            atualizar_mental(-10)
            $ mental += -10,
        
        "Tentar ganhar dinheiro extra com um trabalho temporário":
            atualizar_financeiro(20)
            $ financeiro += 20,
            atualizar_fisico(-10)
            $ fisico += -10,
    
    # Restante do código...