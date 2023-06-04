label agravamento_saude_mae:

    scene mae [1]
    show principal[1] in left
    
    narrador "A saúde da sua mãe está piorando e você precisa encontrar uma maneira de pagar pelos tratamentos médicos."
    
    principal "Mãe, eu amo tanto a senhora, sempre fez de tudo por mim. Me desculpe por estar falhando com a senhora, me desculpa mesmo, eu estou tentando o meu melhor."
    
    menu:
        "Usar todas as economias para pagar pelo tratamento da mãe":
            atualizar_financeiro(-50)
            $ financeira += -50,
            atualizar_mental(-20)
            $ mental += -20,
            atualizar_familia(-20)
            $ familia += -20,
        
        "Pedir ajuda a amigos e familiares":
            atualizar_familia(-10)
            $ familia -10,
    # Restante do código...