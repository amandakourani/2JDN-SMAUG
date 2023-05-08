label cena2:
    image rua = "image/bg/rua.png"
    image escritorio = "image/bg/escritorio.png"


    show rua
    ia "sei que está triste mas não deixe a vida te abalar! Você ainda tem a oportunidade de desenhar seu próprio destino! A meritocracia americana pe maravilhosa, tanto que você pode escolher as opções a seguir: "

    label escolhamenu:

        if passou_por_subescolha_clt == true:
            menu:
                "Vender Bolo de Pote"
                    jump empreender
                
                "Terminar estudos"
                    jump estudo
                
                "entrar pro crime"
                    jump subescolha_crime

        else:
            menu:
                "Arrumar emprego":
                    jump subescolha_clt

                "terminar estudo":
                    jump estudo

                "entrar pro crime":
                    jump subescolha_crime


    label subescolha_clt:
        menu:
            "Entrevista":
                # Ação a ser executada quando a opção "Telemarketing" for escolhida
                # entrevista
                scene escritorio

                show principal[2] in left

                narrator "Qual animal você seria na natureza?"
                input 
                narrator "Cite 1 defeito seu"
                input
                narrator "E 1 qualidade?"
                input
                
                $ empregado == renpy.random.choice(["contratado", "nao contratado", "demitido"])

                if empregado == "contratado":
                    $ contratado = true
                    $ tramporandom = renpy.random.choice(["mcdonalds","telemarketing"])
                
                    if tramporandom == "mcdonalds":
                        #aqui faz o codigo dele trampando no mcdonalds

                    elif tramporandom == "telemarketing":
                        #Aqui faz o codigo do telemarketing
                else:
                    jump volta_pra_casa
                           
            "Vender Bolo de Pote":
                jump empreender

    label empreender:
        #script da venda de bolo de pote


    label estudo:

        # Ação a ser executada quando a opção "terminar estudo" for escolhida


    label subescolha_crime:

        menu:
            "Matar":
                # Ação a ser executada quando a opção "Matar" for escolhida

            "Traficar":
                # Ação a ser executada quando a opção "Traficar" for escolhida


    label volta_pra_casa:

        #financeira = 10
        if contratado == true:
            |#mae feliz, mas ja tem que gastari dinheiro
    

