
dados=None
def opcao1():
    
    global dados

    print("Você selecionou a opção (Registrar um reciclador).")
    # Obtém o número do container, a rua, cidade e estado através de input do usuário
    a = int(input("Digite o número do Reciclador: "))
    b = str(input("Digite a rua do Reciclador: "))
    c = str(input("Digite a cidade: "))
    print("## Reciclador registrado ##")
    dados=[a,c,b]
    

def opcao2(dados):
    
    import requests
    
    a,b,c = dados
    print("Você selecionou a opção 2.")
    print("Buscando reciclador...")

    # URL da API do OpenStreetMap para obter as coordenadas geográficas a partir do endereço
    url = 'https://nominatim.openstreetmap.org/search?q={b},{c}&format=json&limit=1'

    # Faz uma requisição GET para a URL definida acima, com um timeout de 10 segundos para receber a resposta
    response = requests.get(url, timeout=(None, 10))

    # Biblioteca para geolocalização (conversão de endereços em coordenadas)
    from geopy.geocoders import Nominatim

    # Biblioteca para plotar os pontos no mapa
    import matplotlib.pyplot as plt

    # Cria um objeto geolocator com um user_agent personalizado para usar a API do OpenStreetMap
    geolocator = Nominatim(user_agent="my_app")

    # Cria uma lista com as localizações a serem buscadas
    locations = [f"{b},{c},"]

    # Cria uma lista vazia para guardar as coordenadas geográficas de cada localização
    coordinates = []

    # Loop para obter as coordenadas geográficas de cada localização usando o objeto geolocator e a API do OpenStreetMap
    for location in locations:
        loc = geolocator.geocode(location)
        coordinates.append((loc.latitude, loc.longitude))

    # Cria um gráfico de dispersão com as coordenadas geográficas obtidas acima
    plt.scatter([coord[1] for coord in coordinates], [coord[0] for coord in coordinates]) 
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Locais em São Paulo")
    plt.show()

def opcao3(dados):
   
    if dados:
        a,b,c= dados
        opcao3(a,b,c)
    else:
        print("Nenhum reciclador registrado.")

while  True:
    print("_____________________________________")
    print("Selecione uma opção:")
    print("1. Registrar um reciclador")
    print("2. Localizar o reciclador registrado")
    print("3. Exibir o log de opções escolhihas")
    print("4. Sair")
    print("_____________________________________")

    opcao = input("Digite o número da opção desejada: ")
    if opcao == "1":
        opcao1()
    elif opcao == "2":
        opcao2(dados)
    elif opcao == "3":
        opcao3(dados)
    elif opcao == "4":
        print("Tchauuuuuu!")
        break
    else:
        print("Opção Invalida, digite uma opção valida: ")