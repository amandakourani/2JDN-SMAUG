
# Declarando imagens e background
image ia = "images/personagens/ia.png"
image principal = ["images/personagens/principal.png", "images/personagens/principaldecostas.png", "image/personagens/principalentrevistado.png"]
image mae = "images/personagens/mae.png"
image teto do quarto = "images/bg/teto do quarto.png"
image espelho do banheiro = "images/bg/espelho do banheiro.png"
image sala de estar = "images/bg/sala de estar.png"
image teto do quarto = "images/bg/teto do quarto.png"
image bgstart = "image/bg/startmenu.png"


default passou_por_subescolha_clt = False


label start_menu:
    menu:
        "INICIO"
            jump introducao
        "REALIZADORES"
            jump creditos
        "SOBRE O JOGO"
            jump sobre

jump start_menu