
# Declarando imagens e background
image ia = "images/personagens/ia.png"
image principal = ["images/personagens/principal_normal.png", "images/personagens/principal_desesperado.png", "images/personagens/principal_dor_de_cabeca.png", "images/personagens/principal_nervoso.png", "images/personagens/principal_entrevista.png", "images/personagens/principal_demitido.png", "images/personagens/principal_cozinhando.png", "images/personagens/principal_uniforme.png", "images/personagens/principaldecostas.jpg", "images/personagens/principal_contratado.png", "images/personagens/principal_atendente_1.png", "images/personagens/principal_atendente_2.png", "images/personagens/principal_escovando_os_dentes.jpg", "images/personagens/principal_final.jpg"]
=======
image principal = ["images/personagens/principal.png", "images/personagens/principaldecostas.png", "image/personagens/principalentrevistado.png", "image/personagens/principalcozinhamc.png"]
>>>>>>> ceb87adf34c275dbaa4f1fa0bce91e15a07d9ab4
image mae = ["images/personagens/mae.png", "images/bg/mae_acamada.jpg"]
image teto_do_quarto = "images/bg/teto do quarto.png"
image sala_de_estar = "images/bg/sala_de_estar.png"
image teto do quarto = "images/bg/teto do quarto.png"
image bgstart = ["image/bg/menu_choices_op1.png", "image/bg/menu_choices_op2.png"]
image clientemc = ["images/personagens/cliente1costas.png", "images/personagens/cliente2costas.png", "images/personagens/cliente3costas.png"]
image cozinhamcdonalds = "images/bg/cozinhamcdonalds.png"
image rua = ["image/bg/centro_cidade_1.jpg", "image/bg/centro_da_cidade_2.jpg"]
image escritorio = "image/bg/escritorio_baguncado.jpeg"
image chefe = "image/personagens/chefe.png
image homem_oferecendo_dinheiro = "image/personagens/homem_oferecendo_dinheiro.jpg"
image clientemultilaser = "image/personagens/telefonemultilaser.jpg"



label start_menu:
    menu:
        "INICIO":
            jump introducao
        "REALIZADORES":
            jump creditos
        "SOBRE O JOGO":
            jump sobre

jump start_menu

# Função para atualizar a variável financeira
function atualizar_financeiro(valor):
    $ financeiro += valor

# Função para atualizar a variável mental
function atualizar_mental(valor):
    $ mental += valor

# Função para atualizar a variável fisica
function atualizar_fisico(valor):
    $ fisico += valor

# Função para atualizar a variável familia
function atualizar_familia(valor):
    $ familia += valor
#DEFININDO AS VARIAVEIS GLOBAIS

default fisico = 75
default mental = 65
default financeiro = 40
default familia = 80