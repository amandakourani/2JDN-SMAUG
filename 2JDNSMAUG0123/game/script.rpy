
# Declarando imagens e background
image ia = "images/personagens/ia.png"
image principal = ["images/personagens/principal_normal.png", "images/personagens/principal_desesperado.png", "images/personagens/principal_dor_de_cabeca.png", "images/personagens/principal_nervoso.png", "images/personagens/principal_entrevista.png", "images/personagens/principal_demitido.png", "images/personagens/principal_cozinhando.png", "images/personagens/principal_uniforme.png", "images/personagens/principaldecostas.jpg", "images/personagens/principal_contratado.png", "images/personagens/principal_atendente_1.png", "images/personagens/principal_atendente_2.png", "images/personagens/principal_escovando_os_dentes.jpg", "images/personagens/principal_final.jpg"]
image mae = "images/personagens/mae.png"
image teto_do_quarto = "images/bg/teto do quarto.png"
image espelho_do_banheiro = "images/bg/espelho do banheiro.png"
image sala_de_estar = "images/bg/sala de estar.png"
image teto_do_quarto = "images/bg/teto do quarto.png"
image bgstart = "image/bg/startmenu.png"
image clientemc = ["images/personagens/cliente1costas.png", "images/personagens/cliente2costas.png", "images/personagens/cliente3costas.png"]
image cozinhamcdonalds = "images/bg/cozinhamcdonalds.png"
image rua = "image/bg/rua.png"
image escritorio = "image/bg/escritorio.png"
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
    $ financeira += valor

# Função para atualizar a variável mental
function atualizar_mental(valor):
    $ mental += valor

# Função para atualizar a variável fisica
function atualizar_fisica(valor):
    $ fisica += valor

#DEFININDO AS VARIAVEIS GLOBAIS

default fisica = 75
default mental = 65
default financeira = 40
default empregado = ""
default tramporandom = ""
default salario = 0
default passou_por_subescolha_clt = False
default contratado = False
default dia = 0