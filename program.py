import math
# Coordenadas das cidades
cities = [
    (500, 500),
    (354, 968),
    (582, 631),
    (411, 807),
    (153, 112),
    (505, 398),
    (117, 730),
    (854, 568),
    (234, 931),
    (140, 725),
    (499, 319),
    (632, 956),
    (220, 520),
    (86, 12),
    (689, 560),
    (580, 845),
    (984, 339),
    (653, 282),
    (615, 278),
    (840, 501),
    (967, 289),
    (804, 22),
    (795, 741),
    (263, 847),
    (601, 850),
    (150, 800),
    (390, 969),
    (967, 117),
    (279, 909),
    (711, 399),
    (435, 707),
    (949, 661),
    (590, 776),
    (616, 836),
    (414, 335),
    (779, 251),
    (34, 986),
    (567, 90),
    (420, 780),
    (811, 535),
    (868, 563),
    (487, 937),
    (991, 195),
    (938, 91),
    (666, 333),
    (243, 527),
    (247, 770),
    (257, 731),
    (159, 596),
    (23, 1),
    (225, 558),
    (112, 306),
    (965, 492),
    (655, 810),
    (545, 178),
    (467, 143),
    (704, 298),
    (902, 210),
    (111, 303),
    (842, 978),
    (252, 286),
    (481, 122),
    (42, 875),
    (868, 379),
    (624, 785),
    (19, 213),
    (737, 684),
    (854, 931),
    (906, 247),
    (726, 15),
    (905, 787),
    (968, 995),
    (293, 355),
    (592, 311),
    (94, 584),
    (337, 619),
    (902, 561),
    (82, 710),
    (766, 539),
    (602, 185),
    (975, 768),
    (727, 782),
    (136, 946),
    (567, 892),
    (713, 690),
    (445, 631),
    (840, 935),
    (257, 761),
    (616, 98),
    (536, 730),
    (311, 585),
    (164, 43)
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