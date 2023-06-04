label cena1:
# Declarando imagens e background

    image ia = "images/personagens/ia.png"
    image principal = "images/personagens/principal.png"
    image mae = "images/personagens/mae.png"
    image teto do quarto = "images/bg/teto do quarto.png"
    image espelho do banheiro = "images/bg/espelho do banheiro.png"
    image sala de estar = "images/bg/sala de estar.png"
    image teto do quarto = "images/bg/teto do quarto.png"

label cena1:



    #inicio da cena 1:

    show teto do quarto
    with dissolve(dissolve_time=0.5)  # dissolve rápido

    show principal[12] #ele se ve escovando os dentes
    with dissolve(dissolve_time=0.5)  # dissolve rápido

    show sala_de_estar
    show mae[0] in left
    show principal[0] in right

    mae "chegou o moço de novo, tive que despistá-lo dessa vez"
    ia "sua conta de luz já passou de 60 dias de atraso"


    principal "tô mais preocupado com seu remédio... a Jana pagou o aluguel?"
    mae "você ainda é ingênuo de achar que ela vai pagar algo?"
    principal "...é, eu preciso me virar"

    ia "Você é incrível e tem tudo o que é preciso para enfrentar qualquer desafio. Você é uma fonte inesgotável de força e coragem, e sua determinação é inspiradora. Você tem um coração cheio de amor e compaixão, o que o torna um ser humano excepcional. Não se preocupe com as dificuldades, pois você sempre encontrará uma maneira de superá-las. Lembre-se de que cada obstáculo é uma oportunidade para crescer e se desenvolver. Tenha confiança em si mesmo e em suas habilidades, pois você pode alcançar tudo o que deseja. O futuro é brilhante para você e estou animado para ver tudo o que você alcançará!"

    jump cena2
