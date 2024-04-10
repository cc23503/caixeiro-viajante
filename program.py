import math
# Coordenadas das cidades
cities = [
    (500, 500),   # cidade 0
    (826, 465),   # cidade 1
    (359, 783),   # cidade 2
    (563, 182),   # cidade 3
    (547, 438),   # cidade 4
    (569, 676),   # cidade 5
    (989, 416),   # cidade 6
    (648, 750),   # cidade 7
    (694, 978),   # cidade 8
    (493, 969),   # cidade 9
    (175, 89),    # cidade 10
    (104, 130),   # cidade 11
    (257, 848),   # cidade 12
    (791, 249),   # cidade 13
    (952, 204),   # cidade 14
    (34, 654),    # cidade 15
    (89, 503),    # cidade 16
    (548, 964),   # cidade 17
    (492, 34),    # cidade 18
    (749, 592),   # cidade 19
    (536, 875),   # cidade 20
    (373, 708),   # cidade 21
    (385, 260),   # cidade 22
    (560, 751),   # cidade 23
    (304, 516),   # cidade 24
    (741, 368),   # cidade 25
    (59, 131),    # cidade 26
    (154, 681),   # cidade 27
    (425, 456),   # cidade 28
    (885, 783),   # cidade 29
    (30, 415),    # cidade 30
    (61, 25)      # cidade 31
]


def assign_city_numbers(cities): #retorna um vetor de 1 até o total de cidades

    city_numbers = list(range(1, len(cities) + 1))
    return city_numbers

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def divide_by_salesmen(salesmen_count):
    city_numbers = assign_city_numbers(cities)
    salesmen_routes = [[] for _ in range(salesmen_count)]  

    for i, city_number in enumerate(city_numbers):
        salesman_index = i % salesmen_count
        salesmen_routes[salesman_index].append(city_number)

    for route in salesmen_routes:
        route.insert(0, 1)  # Insert city 1 at the beginning
        route.append(1)  # Append city 1 at the end

    for i, route in enumerate(salesmen_routes):
        print(f"Salesman {i + 1}: {route}")
    return salesmen_routes

def total_distance(route):
    """calculates the total distance traveled for a given route. route : List of city numbers representing the route. returns distance traveled for the route."""
    total = 0
    for i in range(len(route) - 1):
        city1 = cities[route[i] - 1]
        city2 = cities[route[i + 1] - 1]
        total += euclidean_distance(city1, city2)
    return total

salesmen_count = 5

salesmen_routes = divide_by_salesmen(salesmen_count)

for i, route in enumerate(salesmen_routes):
    print(f"Salesman {i + 1} total distance: {round(total_distance(route))}")
