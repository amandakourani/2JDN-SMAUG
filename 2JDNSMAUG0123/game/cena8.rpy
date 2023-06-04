label luta_continua:

    scene rua_movimentada
    show principal[determinado, cuidado] in center
    
    narrator "Você está lutando para sobreviver e cuidar da sua família. A luta de classes é dura, mas você está disposto a enfrentar todos os desafios."
    
    menu:
        "Continuar trabalhando duro e cuidando da saúde":
            increase_health(10)
            increase_financial(10)
            jump final_cansado_onibus
        
        "Desistir e perder a esperança":
            decrease_health(10)
            decrease_financial(10)
            jump final_desacordado

label final_cansado_onibus:

    scene onibus
    show principal[cansado] in center
    
    narrator "A luta de classes é implacável, mas você conseguiu sobreviver e cuidar da sua família. Apesar de não ter atingido 100% em todas as variáveis e não ter alcançado o objetivo de 1 milhão de reais, você provou que a luta é possível. Parabéns, guerreiro."
    end_game()

label final_desacordado:

    scene quarto
    show principal[caido] in center
    
    narrator "Infelizmente, a pressão da luta de classes foi demais para você. Você desistiu e perdeu a esperança. Seu corpo cedeu, deixando-o desacordado. Sua saúde está em zero e suas finanças estão em 100. Lembre-se, a luta é difícil, mas sempre há esperança."
    end_game()

