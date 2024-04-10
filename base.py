import math

#cidade coordinates
cities = [
    (1, 2),  # cidade 1
    (4, 5),  # cidade 2
    (7, 8),  # cidade 3
    (3, 1),  # cidade 4
    (8, 4),  # cidade 5
    (2, 6),  # cidade 6
    (5, 9),  # cidade 7
]
odd_salesman = []
even_salesman = []

def assign_city_numbers(cities): # Transforma as coordenadas em uma lista de 1 até a quantidade de cidades(7)
    city_numbers = []
    for i in range(1, len(cities) + 1): # Começa na posição 1, porque a 0 será a cidade 1, e depois adiciona a 1 novamente no fim
        city_numbers.append(i)
    return city_numbers

def divide_trips_even_odd(city_numbers): # Função para separar as cidades pares e as ímpares
    even_salesman = [city_numbers[0]] + [city for city in city_numbers if city % 2 == 0] + [city_numbers[0]] # 1o CITY é o valor que iremos incluir, e o 2o é uma variável temporária, como um "i"
    odd_salesman = [city_numbers[0]] + [city for city in city_numbers if city % 2 != 0 and city>1] + [city_numbers[0]] # >1 é para não incluir a cidade de início (1) a lista
    return even_salesman, odd_salesman

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) # sqrt ~= squareRoot(raiz quadrada)

def nearest_neighbor_route(city_numbers, cities): # mais próximo para menores distâncias, ímpares e pares
    route = [city_numbers[0]]
    current_city = city_numbers[0]
    unvisited_cities = set(city_numbers[1:-1])  # Ignorando a primeira e a última cidade, pois elas são fixas
    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: euclidean_distance(cities[current_city - 1], cities[city - 1]))
        route.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city
    route.append(city_numbers[0])  # Adicionando a cidade inicial novamente no final da rota
    return route

def calculate_and_display_distances(route, cities):
    total_distance = 0
    for i in range(len(route) - 1): #vai até menos 1 pq a ultima distancia do vetor já é 1, então o calculo da ultima cidade de volta para a 1 é calculada aqui.
        distance = euclidean_distance(cities[route[i] - 1], cities[route[i + 1] - 1])
        total_distance += distance
    print(round(total_distance,2), "unidades")
    return total_distance

 
city_numbers = assign_city_numbers(cities)
print(city_numbers)

even_salesman, odd_salesman = divide_trips_even_odd(city_numbers)
print("\nCaixeiro par:", even_salesman)
print("Caixeiro ímpar:", odd_salesman)

best_route_even = nearest_neighbor_route(even_salesman, cities)
best_route_odd = nearest_neighbor_route(odd_salesman, cities)
print("\nMelhor rota para o caixeiro par:", best_route_even)
print("Melhor rota para o caixeiro ímpar:", best_route_odd)

print("\nDistância total do caixeiro par: ")
total_distance_even = calculate_and_display_distances(best_route_even, cities)

print("\nDistância total do caixeiro ímpar: ")
total_distance_odd = calculate_and_display_distances(best_route_odd, cities)

print("\nDistância total:\n", round(total_distance_even + total_distance_odd,2), "unidades")