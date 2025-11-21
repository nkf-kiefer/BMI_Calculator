# -- importando o módulo de quebra de texto -- 
import textwrap


# -- Bloco de cores --
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
ORANGE = "\033[38;5;208m"
WHITE = "\033[97m"


# -- Bloco de declaração de variaveis mutáveis --
abaixo_peso = peso_normal = sobrepeso = obeso_1 = obeso_2 = obeso_3 = 0
pacientes = []
maior_peso = 0
quantidade_de_pessoas = 0


# -- Bloco de saudação inicial -- 
print(BOLD + BLUE + "=" * 80 + RESET)
print(BOLD + WHITE + " SEJA BEM VINDO(A) A CALCULADORA DE IMC ".center(80) + RESET)
print(BOLD + BLUE + "=" * 80 + RESET)
print(BOLD + CYAN + "Caso queira parar o programa basta digitar 0!".center(80) + RESET)
print(BOLD + BLUE + "-" * 80 + RESET)


# -- Enquanto o médico não digitar 100 na altura ou no peso -- 
while True:
    try:
        # -- Coletando os dados -- 
        nome = str(input(BOLD + YELLOW +"Digite o nome do(a) paciente: " + RESET))
        peso = float(input("Digite o seu peso: "))
        altura = float(input("Digite a sua altura: "))

        # -- Se quiser encerrar -- 
        if peso == 0 or altura == 0 or nome == 0 :
            print(BOLD + RED + "programa encerrado" + RESET)
            break

        # -- calculo do imc -- 
        calculadora_imc = round(peso / (altura**2), 2)

        # -- armazenando o valor do imc em uma váriavel -- 
        valor_imc = calculadora_imc

        # -- cálculo do peso minimo e maximo ideal -- 
        peso_ideal = round(18.6 * (altura**2), 2)
        peso_ideal_max = round(24.9 * (altura**2), 2)

        # -- inciando a verificação da classificação do imc -- 
        if valor_imc <= 18.5:
            classificacao = 'abaixo do peso'
            mensagem = "Procure um nutricionista e um médico para entender mais da sua saúde!"
            abaixo_peso += 1
        elif valor_imc <= 24.9:
            classificacao = 'peso saúdavel'
            mensagem = "Parabéns, continue se cuidando!"
            peso_normal += 1
        elif valor_imc <= 29.9:
            classificacao = "sobrepeso"
            mensagem = "Busque evitar consumir alimentos ruins para a saúde e muito cáloricos"
            sobrepeso += 1
        elif valor_imc <= 34.9:
            classificacao = "Obesidade grau 1"
            mensagem = "Busque o auxílio de um nutricionista além de realizar a prática de exercícios físicos"
            obeso_1 += 1
        elif valor_imc <= 39.9:
            classificacao = "Obesidade grau 2"
            mensagem = 'Busque ajuda médica antes que seja mais difícil reverter a obesidade'
            obeso_2 += 1
        else: 
            classificacao = "Obesidade grau 3"
            mensagem = 'Busque ajuda médica o quanto antes para que sua saúde seja restabelecida! '
            obeso_3 += 1
        
        # -- Quantas vezes o sistema rodar armazenar quantas vezes rodou -- 
        quantidade_de_pessoas += 1
        
        # -- mostrando a cada vez que o looping rodar os valores do paciente especifico -- 
        print(BOLD + BLUE + "\n" + "=" * 60 + RESET)
        print(BOLD + WHITE + f"Resultado de {nome.upper()}".center(60) + RESET)
        print(BOLD + BLUE + "=" * 60 + RESET)
        print(f"{WHITE}IMC calculado: {BOLD}{valor_imc}{RESET}")
        print(f"{WHITE}Classificação: {BOLD}{classificacao}{RESET}")
        print(f"{WHITE}Peso ideal mínimo: {BOLD}{peso_ideal} kg{RESET}")
        print(f"{WHITE}Peso ideal máximo: {BOLD}{peso_ideal_max} kg{RESET}")
        recomendacao_formatada = "\n".join(textwrap.wrap(mensagem, width=40))
        print(f"{BOLD}Recomendação:{RESET} {recomendacao_formatada}")
        print(BOLD + BLUE + "-" * 60 + RESET)

        # -- armazenando os valores dos pacientes em um dicionário -- 
        pacientes.append({
            'nome' : nome,
            'peso' : peso,
            'altura': altura,
            'IMC': valor_imc,
        })        
    
    # -- Se o usuário realizar uma entrada indevida como texto -- 
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
    except KeyboardInterrupt:
        print("Encerrando o programa")
        break

# -- Melhorando a visualização das estatísticas --    
# -- percorrendo os pacientes (se tiver) e coletando dados --
if pacientes:
    peso = [i['peso'] for i in pacientes]
    altura = [i['altura'] for i in pacientes]
    imc = [i['IMC'] for i in pacientes]

    maior_peso = max(peso)
    menor_peso = min(peso)
    maior_altura = max(altura)
    menor_altura = min(altura)
    maior_imc = max(imc)
    menor_imc = min(imc)

    # -- calculando a media de imc pela quantidade de pessoas -- 
    media_imc = round(sum(imc) / quantidade_de_pessoas,2)
        

    # -- Bloco para mostrar os resultados -- 
    print("\n" + BOLD + CYAN + "=" * 80 + RESET)
    print(BOLD + WHITE + "RESUMO GERAL DOS PACIENTES".center(80) + RESET)
    print(BOLD + CYAN + "=" * 80 + RESET)
    print(f"{YELLOW}Abaixo do peso:{RESET} {abaixo_peso}")
    print(f"{GREEN}Peso normal:{RESET} {peso_normal}")
    print(f"{ORANGE}Sobrepeso:{RESET} {sobrepeso}")
    print(f"{RED}Obesidade grau 1:{RESET} {obeso_1}")
    print(f"{RED}Obesidade grau 2:{RESET} {obeso_2}")
    print(f"{MAGENTA}Obesidade grau 3:{RESET} {obeso_3}\n")

    print(f"{WHITE}Maior peso: {BOLD}{maior_peso} kg{RESET}")
    print(f"{WHITE}Menor peso: {BOLD}{menor_peso} kg{RESET}")
    print(f"{WHITE}Maior altura: {BOLD}{maior_altura} m{RESET}")
    print(f"{WHITE}Menor altura: {BOLD}{menor_altura} m{RESET}")
    print(f"{WHITE}Maior IMC: {BOLD}{maior_imc}{RESET}")
    print(f"{WHITE}Menor IMC: {BOLD}{menor_imc}{RESET}")
    print(f"{WHITE}Média geral de IMC: {BOLD}{CYAN}{media_imc}{RESET}")

    print(BOLD + BLUE + "\n" + "=" * 80 + RESET)
    print(BOLD + WHITE + " FIM DO RELATÓRIO ".center(80) + RESET)
    print(BOLD + BLUE + "=" * 80 + RESET)
