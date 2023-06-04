label dilema_financeiro:

    scene mesa_contas
    show principal[preocupado] in left
    
    narrador "As contas estão chegando e você precisa decidir o que pagar primeiro."
    
    menu:
        "Pagar o aluguel antes que seja tarde demais":
            atualizar_financeiro(-20)
            atualizar_saude(-10)
        
        "Pagar a conta de luz para evitar cortes":
            atualizar_financeiro(-10)
            atualizar_saude(-5)
    
    menu:
        "Pedir um empréstimo com juros altos":
            atualizar_financeiro(-30)
            atualizar_saude(10)
        
        "Tentar ganhar dinheiro extra com um trabalho temporário":
            atualizar_financeiro(+20)
            atualizar_saude(-10)
    
    # Restante do código...