label subescolha_crime:

    if passou_por_subescolha_clt == True:
        jump demissao
        
    menu:
        "Roubar":
            # Ação a ser executada quando a opção "Roubar" for escolhida

            label escolha_crime:
    narrador "principal decide entrar para o mundo do crime."

            "Traficar":
                # Ação a ser executada quando a opção "Traficar" for escolhida
    menu:
        "1. Roubar. (+500 no financeiro, -50 na mental)":
           
            atualizar_financeiro(500)
            $ financeiro += 500,
            atualizar_mental(-50)
            $ saude += -50,

            jump resultado_roubar

        "2. Traficar. (+300 na carteira, -20 na saúde)":

            atualizar_financeiro(300)
            $ financeiro += 300,
            atualizar_mental(-20)
            $ mental += -20
            jump resultado_traficar

label resultado_roubar:
    narrador "principal se envolve em atividades criminosas, entrando na gangue da bicicleta que age no centro de São Paulo. Sabendo que está roubando os bens de pessoas trabalhadoras, e trazendo sofrimento para elas, ele vai ficando cada vez mais ansioso e depressivo."

    principal "Eu não sou uma pessoa má, eu preciso fazer isso para salvar a minha mãe.
    "
    jump proxima_fase

label resultado_traficar:
   narrador "principal se envolve no tráfico de drogas para ganhar dinheiro. Apesar de estar fazendo mais grana, saber que está vendendo k9 para as pessoas e isso vem matando várias, acaba te matando por dentro, tantas vidas perdidas..."

    jump proxima_fase

label proxima_fase:
    # aqui você pode escrever o código para a próxima fase do jogo