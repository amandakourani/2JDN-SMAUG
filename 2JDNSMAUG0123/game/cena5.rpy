label consequencias_trabalho_corpo:

    scene casa
    show principal[cansado] in left
    
    if passou_por_subescolha_clt == True:
        ia "Pare de mimimi e vá trabalhar seu vagabundo. Está achando que assim você conseguirá algo em sua vida?"
        pause 0.5
        narrator "O personagem principal se olha no espelho enquanto vê sua aparência cansada, seus olhos estão fundos, sua pele cheia de marcas de expressão. Você vê a tristeza em seu rosto, sabendo que terá que sobreviver ao inferno novamente amanhã."
        principal "Estou tão cansado, não quero mais ir para aquele lugar, não quero mais ter que fazer nada. Gostaria de parar de existir."
        atualizar_saude(-15)
    
    elif passou_por_subescolha_empreendedorismo == True:
        ia "O que aconteceu que você ainda não está produzindo seus bolos? Vamos para mais um dia de sucesso!"
        show principal[cansado] in left
        narrator "Seus pés estão cheios de bolhas, suas mãos com calos de tanto carregar a bolsa térmica e seus ombros cansados devido ao peso."
        principal "Será que vale a pena eu me matar para conseguir tão pouco retorno? Achei que seria diferente, vejo pessoas empreendendo no TikTok e vencendo, por que comigo isso não acontece?"
        atualizar_saude(-10)
    
    elif passou_por_subescolha_crime == True:
        show principal[triste] in left
        principal "Sei que o que estou fazendo é errado. Me sinto tão culpado, estou com crises constantes de ansiedade, pois minha vida agora é prejudicar as outras pessoas. Será que o dinheiro vale a pena?"
        ia "Deixe de choradeira!"
        atualizar_saude(-15)
    
    # Restante do código...
