label cena2:
    image rua = "image/bg/rua.png"


    show rua
    ia "sei que está triste mas não deixe a vida te abalar! Você ainda tem a oportunidade de desenhar seu próprio destino! A meritocracia americana pe maravilhosa, tanto que você pode escolher as opções a seguir: "

    label menu:
        menu:
            "Arrumar emprego":
                jump subescolha_clt

            "terminar estudo":
                jump escola

            "entrar pro crime":
                jump subescolha_crime


    label subescolha_clt:
        menu:
            "Telemarketing":
                # Ação a ser executada quando a opção "Telemarketing" for escolhida
                # entrevista
                

            "Mcdonalds":
                # Ação a ser executada quando a opção "Mcdonalds" for escolhida

            "Vender Bolo de Pote":



    label escola:

        # Ação a ser executada quando a opção "terminar estudo" for escolhida e o personagem voltar triste para casa


    label subescolha_crime:

        menu:
            "Matar":
                # Ação a ser executada quando a opção "Matar" for escolhida

            "Traficar":
                # Ação a ser executada quando a opção "Traficar" for escolhida


    label volta_pra_casa:
