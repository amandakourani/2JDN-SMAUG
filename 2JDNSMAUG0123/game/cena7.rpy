label agravamento_saude_mae:

    scene quarto_mae
    show principal[preocupado, chorando] in left
    
    narrator "A saúde da sua mãe está piorando e você precisa encontrar uma maneira de pagar pelos tratamentos médicos."
    
    principal "Mãe, eu amo tanto a senhora, sempre fez de tudo por mim. Me desculpe por estar falhando com a senhora, me desculpa mesmo, eu estou tentando o meu melhor."
    
    menu:
        "Usar todas as economias para pagar pelo tratamento da mãe":
            decrease_financial(50)
            decrease_health(20)
            decrease_family(20)
        
        "Pedir ajuda a amigos e familiares":
            decrease_family(10)
    
    # Restante do código...